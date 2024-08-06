import requests
import json
from config import API_KEY, ACCOUNT_ID

HEADERS = {
    'Content-Type': 'application/json',
    'API-Key': API_KEY,
}

NERDGRAPH_URL = "https://api.newrelic.com/graphql"

def run_query(query):
    response = requests.post(NERDGRAPH_URL, headers=HEADERS, data=json.dumps({"query": query}))
    if response.status_code == 200:
        result = response.json()
        if "errors" in result:
            print("Errors:", result["errors"])
            return None
        return result
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {response.text}")
    
def read_policies(file_path):
    with open(file_path) as f:
        return json.load(f)    