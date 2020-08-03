import requests
import base64
import json

usr = ""
pwd = ""
org = "person-eval"

auth = base64.b64encode(f"{usr}:{pwd}".encode("utf8")).decode("utf8")

# create target server for backend

for env in ["test", "prod"]:
    req = requests.request(
        "POST",
        f"https://api.enterprise.apigee.com/v1/organizations/{org}/environments/{env}/targetservers",
        headers={
            "Authorization": f"Basic {auth}"
        },
        json={
            "name" : "boerse-frankfurt-api-backend",
            "host" : "api.boerse-frankfurt.de",
            "isEnabled" : True,
            "port" : 443,
            "sSLInfo": {
                "enabled": True
            }
        }
    )

# create product for production use

req = requests.request(
    "POST",
    f"https://api.enterprise.apigee.com/v1/organizations/{org}/apiproducts",
    headers={
        "Authorization": f"Basic {auth}"
    },
    json={
        "name": "product-stock-exchange-info-api",
        "displayName": "Product Stock Exchange Info API",
        "approvalType": "manual",
        "attributes": [
            {
                "name": "access",
                "value": "public"
            }
        ],
        "description": "",
        "apiResources": [],
        "environments": ["prod"],
        "proxies": ['boerse-frankfurt-de'],
        "quota": "50",
        "quotaInterval": "1",
        "quotaTimeUnit": "minute",
        "scopes": []
    }
)

# create encrypted KVM and store value for loggly token
# ...