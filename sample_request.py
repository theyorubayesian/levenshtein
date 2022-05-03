import requests

url = "http://localhost:7071/validate-name/"

# -----------------
# Single Validation
# -----------------
sample = {
    "first_name": "Jumia Plc.",
    "middle_name": "",
    "surname": ""
}
print(sample)

response = requests.post(url, json=sample,  headers={"Content-type": "application/json"})
print(response.text)
print("Status Code: ", response.status_code)
print("Result: ", response.json())

# ----------------
# Batch Validation
# ----------------
url = "http://localhost:7071/validate-names/"
samples = {
    "customers": [sample, sample]
}
print(samples)

response = requests.post(url, json=samples,  headers={"Content-type": "application/json"})
print(response.text)
print("Status Code: ", response.status_code)
print("Result: ", response.json())
