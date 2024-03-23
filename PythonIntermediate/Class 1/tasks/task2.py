import csv

import requests


def convert_list(list, key='name'):
    new_list = []
    for item in list:
        r_item = requests.get(item, headers={"User-Agent": user_agent})
        new_list.append(r_item.json()[key])

    return new_list


def process_data(data):
    for person in data:
        homeworld = person['homeworld']
        r_homeworld = requests.get(homeworld, headers={"User-Agent": user_agent})
        person['homeworld'] = r_homeworld.json()['name']

        person['films'] = convert_list(person['films'], 'title')
        person['species'] = convert_list(person['species'])
        person['vehicles'] = convert_list(person['vehicles'])
        person['starships'] = convert_list(person['starships'])

    return data


user_agent = 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
try:
    r = requests.get("https://swapi.dev/api/people", headers={"User-Agent": user_agent})
    results = process_data(r.json()['results'])
    next_page = r.json()['next']
    while next_page is not None:
        r = requests.get(next_page, headers={"User-Agent": user_agent})
        results.extend(process_data(r.json()['results']))
        next_page = r.json()['next']

except Exception as e:
    print(e)
    results = {}

print(results)
with open('api_output_detailed.csv', 'w', newline='', encoding='UTF-8') as output:
    headers = results[0].keys()
    writer = csv.DictWriter(output, fieldnames=headers)

    writer.writeheader()
    writer.writerows(results)
