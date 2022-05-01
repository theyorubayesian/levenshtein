import requests

url = "http://127.0.0.1:8000/validate-name/"

sample = {
    "first_name": "Jumia Plc.",
    "middle_name": "",
    "surname": ""
}
print(sample)

response = requests.post(url, json=sample,  headers={"Content-type": "application/json"})
print(response.text)
print("Status Code: ", response.status_code)
print("Reason: ", response.reason)
