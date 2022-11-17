import requests
import json



response = requests.get('https://api.goperigon.com/v1/all?apiKey=08db32cd-ff74-4992-959b-3b2a0899d564&q="Catherine Cortez-Masto" &showReprints=false&from=2022-01-01&to=2022-01-31').text
response_info = json.loads(response)

print(response_info)