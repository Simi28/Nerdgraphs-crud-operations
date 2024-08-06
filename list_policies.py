from sharedcode import run_query
from config import ACCOUNT_ID

def list_alert_policies():
    query = f"""
    {{
      actor {{
        account(id: {ACCOUNT_ID}) {{
          alerts {{
            policiesSearch {{
              policies {{
                id
                name
                incidentPreference
              }}
            }}
          }}
        }}
      }}
    }}
    """
    return run_query(query)

if __name__ == "__main__":
    policies = list_alert_policies()
    if policies:
        for policy in policies['data']['actor']['account']['alerts']['policiesSearch']['policies']:
            print(f"Policy ID: {policy['id']}, Name: {policy['name']}")
    else:
        print("Failed to list policies")
