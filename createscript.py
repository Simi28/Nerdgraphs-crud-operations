from sharedcode import run_query, read_policies
from config import ACCOUNT_ID
    
def create_alert_policy(name, incident_preference):
    mutation = f"""
    mutation {{
      alertsPolicyCreate(
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

# Create policies
for policy in policies:
        name = policy["name"]
        incident_preference = policy["incidentPreference"]
        create_response = create_alert_policy(name, incident_preference)
        if create_response:
            print(f"Created Policy with Name: {name} and Incident Preference: {incident_preference}")
        else:
            print(f"Failed to create policy with Name: {name}")