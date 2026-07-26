import requests

API_URL = "https://cloud.flowiseai.com/api/v1/prediction/446381bf-d5ef-47e1-8934-20184cfb6ed5"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

output = query({
    "question": "Give me detailed recipe for chocolate mousse",
})

print(output["text"])