import requests
from flask import current_app as app

OPA_URL = "http://opa:8181/v1/data/example/authz/allow"

def check_opa(role, method):
    input_data = {
        "input": {
            "role": role,
            "method": method
        }
    }
    try:
        response = requests.post(OPA_URL, json=input_data)
        response.raise_for_status()
        result = response.json()
        app.logger.debug(f"OPA response: {result}")
        return result.get("result", False)
    except requests.RequestException as e:
        app.logger.error(f"OPA request failed: {e}")
        return False
