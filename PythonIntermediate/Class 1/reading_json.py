import json

with open('json_source.json', 'r') as file:
    data = json.load(file)

print(data)

with open('json_output.json', 'w') as output:
    json.dump(data, output, indent=4)
