# Azure-Governance-via-Python-Policy-as-Code---Virtual-Machine
This project demonstrates how to programmatically manage Azure Governance using the Azure Python SDK. It automates the deployment of Azure Policies to enforce cost controls and organizational standards.

🚀 Features
Cost Guardrails: Automatically denies the creation of Virtual Machines unless they use the Standard_B1s size.

Tag Enforcement: (In Progress) Ensures every resource is created with an Environment tag for better billing tracking.

Automated Authentication: Uses DeviceCodeCredential to handle secure logins across multiple tenants (Work vs. Personal).

🛠️ Tech Stack

Language: Python 3.x

Cloud: Microsoft Azure

Libraries:

azure-identity: For secure authentication.

azure-mgmt-resource: For interacting with Azure Policy services.

📋 Prerequisites
An active Azure Subscription.

Python installed on your local machine.

Libraries installed via pip:

Bash
pip install azure-identity azure-mgmt-resource-policy
⚙️ Setup & Usage
Clone this repository.

Update the SUBSCRIPTION_ID and TENANT_ID variables in the scripts.

Run the deployment script:

Bash
   python deploy_policy.py
Follow the terminal instructions to authenticate via the browser.

🛡️ Verification
The policy can be verified in the Azure Portal under the Policy > Assignments tab. Any attempt to create a VM larger than a B1s will be blocked at the validation stage by the Azure Resource Manager.
