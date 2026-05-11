# Azure Automated Governance: Policy-as-Code

This project demonstrates how to use **Python** and the **Azure SDK** to automate cloud governance. By deploying custom Azure Policies, this script establishes "guardrails" to prevent high costs and ensure organizational compliance.

## 🛡️ Implemented Guardrails
1.  **VM Size Restriction**: Automatically denies the creation of any Virtual Machine unless the size is `Standard_B1s`.
2.  **Tag Enforcement**: Denies the creation of any resource that does not include the `Environment` tag (used for cost tracking).

## 🛠️ Technology Stack
*   **Language**: Python 3.x
*   **SDK**: `azure-mgmt-resource`, `azure-identity`
*   **Authentication**: `InteractiveBrowserCredential` with Multi-Tenant support.

## 🚀 How to Use
1.  **Clone the Repo**: Download the `deploy_governance.py` file.
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

## 🔍 Why this matters
In a real-world enterprise environment, manual oversight is impossible. This project solves that by:
*   **Preventing Cost Overruns**: No one can accidentally spin up a $500/month VM.
*   **Standardizing Data**: Every resource is forced to have an 'Environment' tag, making billing reports accurate.
*   **Automation**: Policies are deployed in seconds across a subscription without clicking through the Portal.

## ✅ Verification
Verification is performed by attempting to create a non-compliant resource in the Azure Portal. The "Validation" step will fail with a `RequestDisallowedByPolicy` error, proving the Python-deployed guardrails are active.


## 📸 Project Evidence

### 1. Policies Created via Python
This screenshot shows the custom policies successfully injected into the Azure environment by the script.
![Policies Created](/screenshots/Policy_page.png)

### 2. VM Size Enforcement (Deny)
Evidence of the 'Cost Guardrail' blocking the creation of a non-compliant VM size.
![VM Size Validation](/screenshots/other_size_blocked_by_policy.png)

### 3. Tag Requirement Enforcement
Evidence of the 'Organization Guardrail' blocking a resource that is missing the Environment tag.
![Tag Validation](/screenshots/resource-creation-failed-no-tags.png)
