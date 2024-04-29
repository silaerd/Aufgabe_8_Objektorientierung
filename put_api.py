import requests
import json

# Define the URL of the API
url = "http://127.0.0.1:5000/"

# Define the data you want to send
data = {
    "name": "TestName"
}

# Convert the data to JSON format
data_json = json.dumps(data)

# Send a POST request to the API
response = requests.put(url, data=data_json)

# Print the response from the server
print(response.text)