from azure.identity import InteractiveBrowserCredential
from azure.mgmt.resource.policy import PolicyClient

# 1. Setup specific IDs
TENANT_ID = "<tenant_id>"
SUBSCRIPTION_ID = "<subscription id>"

# 2. Force the login to the correct directory
credential = InteractiveBrowserCredential(
    tenant_id=TENANT_ID, 
    prompt="select_account"
)
client = PolicyClient(credential, SUBSCRIPTION_ID)

try:
    print(f"Connecting to Tenant: {TENANT_ID}")
    #policy_client = PolicyClient(credential, SUBSCRIPTION_ID)
    
    print("Login successful! Defining the policy logic...")

    vm_rule = {
        "if": {
            "allOf": [
                { "field": "type", "equals": "Microsoft.Compute/virtualMachines" },
                { "field": "Microsoft.Compute/virtualMachines/sku.name", "notEquals": "Standard_B1s" }
            ]
        },
        "then": { "effect": "deny" }
    }

    # --- POLICY 2: REQUIRE TAG ---
    tag_rule = {
        "if": {
            "field": "tags['Environment']",
            "exists": "false"
        },
        "then": { "effect": "deny" }
    }

    policies = [
        {"name": "LimitVMSize", "display": "Limit VM Size to B1s(Created via Python)", "rule": vm_rule},
        {"name": "RequireTag", "display": "Require Environment Tag(Created via Python)", "rule": tag_rule}
    ]

    for p in policies:
        print(f"Deploying: {p['display']}...")
        
        # Create Definition
        defn = client.policy_definitions.create_or_update(
            p['name'],
            {
                "policy_rule": p['rule'],
                "display_name": p['display'],
                "policy_type": "Custom"
            }
        )

        # Create Assignment
        client.policy_assignments.create(
            scope=f"/subscriptions/{SUBSCRIPTION_ID}",
            policy_assignment_name=f"Assign_{p['name']}",
            parameters={
                "policy_definition_id": defn.id,
                "display_name": f"Enforced: {p['display']}"
            }
        )

    print("\nAll guardrails are live!")

except Exception as e:
    print(f"An error occurred: {e}")
