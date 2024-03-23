import csv

import requests

user_agent = 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
try:
    r = requests.get("https://swapi.dev/api/people", headers={"User-Agent": user_agent})
    results = r.json()['results']
    next_page = r.json()['next']
    while next_page is not None:
        r = requests.get(next_page, headers={"User-Agent": user_agent})
        results.extend(r.json()['results'])
        next_page = r.json()['next']

except Exception as e:
    print(e)
    results = {}

with open('api_output.csv', 'w', newline='') as output:
    headers = results[0].keys()
    writer = csv.DictWriter(output, fieldnames=headers)

    writer.writeheader()
    writer.writerows(results)
