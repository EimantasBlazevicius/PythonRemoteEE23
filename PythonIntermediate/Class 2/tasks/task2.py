import csv
import json

with open('data.csv', 'r') as f:
    data = []
    headers = []
    reader = csv.reader(f)
    for index, item in enumerate(reader):
        new_object = {}
        if index == 0:
            headers = [value.strip() for value in item]
        else:
            for index, value in enumerate(item):
                new_object[headers[index]] = value.strip() if not value.strip().isnumeric() else int(value.strip())
            data.append(new_object)
with open('result.json', 'w') as output:
    json.dump(data, output, indent=4)
