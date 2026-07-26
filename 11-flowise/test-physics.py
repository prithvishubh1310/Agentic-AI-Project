import requests

API_URL = "https://cloud.flowiseai.com/api/v1/prediction/446381bf-d5ef-47e1-8934-20184cfb6ed5"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

output = query({
    "question": "provide me answer if there is a square each side is of 10 cm what is the area of square?",
})

print(output["text"])
