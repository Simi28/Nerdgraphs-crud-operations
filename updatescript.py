from sharedcode import run_query, read_policies
from config import ACCOUNT_ID,API_KEY

def update_alert_policy(policy_id, name, incident_preference):
    mutation = f"""
    mutation {{
      alertsPolicyUpdate(
        id: "{policy_id}"
        accountId: {ACCOUNT_ID}
        policy: {{
          name: "{name}"
          incidentPreference: {incident_preference}
        }}
      ) {{
        id
        name
      }}
    }}
    """
    return run_query(mutation)

if __name__ == "__main__":
    policies = read_policies('policies.json')

    for policy in policies:
        policy_id = policy["id"].strip() 
        name = policy["name"]
        incident_preference = policy["incidentPreference"]
        print(f"Attempting to update policy ID: {policy_id} with Name: {name} and Incident Preference: {incident_preference}")  # Debug: print policy details
        update_response = update_alert_policy(policy_id, name, incident_preference)
        if update_response:
            print(f"Updated Policy ID: {policy_id} to Name: {name} with Incident Preference: {incident_preference}")
        else:
            print(f"Failed to update policy ID: {policy_id}")
