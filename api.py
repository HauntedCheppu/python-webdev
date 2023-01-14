import json
import requests

response = requests.get("https://hub.dummyapis.com/vj/qqw0LnQ")

print(response.status_code)
res = json.loads(response.text)

for data in res:
    print(data)
