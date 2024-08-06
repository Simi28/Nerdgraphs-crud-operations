from sharedcode import run_query, read_policies
from config import ACCOUNT_ID

def delete_alert_policy(policy_id):
    mutation = f"""
    mutation {{
      alertsPolicyDelete(
        id: "{policy_id}"
        accountId: {ACCOUNT_ID}
      ) {{
        id
      }}
    }}
    """
    return run_query(mutation)

if __name__ == "__main__":
  policies = read_policies('policies.json') 
# Delete policies
for policy in policies:
        policy_id = policy["id"]
        delete_response = delete_alert_policy(policy_id)
        if delete_response:
            print(f"Deleted Policy ID: {policy_id}")
        else:
            print(f"Failed to delete policy ID: {policy_id}")