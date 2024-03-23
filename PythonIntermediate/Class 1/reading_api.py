import json

import requests

base_api = "https://swapi.dev/api"
user_agent = 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
try:
    r = requests.get(f"{base_api}/people", headers={"User-Agent": user_agent})
    results = r.json()['results']
    print(results)

    with open('api_output.json', 'w') as output:
        json.dump(results, output, indent=4)
except Exception as e:
    print(e)
    results = {}

with open('api_output.json', 'w') as output:
    json.dump(results, output, indent=4)
