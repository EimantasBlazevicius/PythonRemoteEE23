import json

sample_dict = {
    "name": "Eimantas",
    "age": 30,
    "city": "Vilnius",
    "cats": ["Yoda", "Obi"],
    "family": [
        {
            "name": "Mantas",
            "age": 27
        },
        {
            "name": "Daugirdas",
            "age": 2
        }
    ],
    "married": True
}

# Add new Key, Value pair
sample_dict['favorite_color'] = "Blue"
# Adjust existing key, value pairs
sample_dict['age'] += 1
sample_dict['cats'].append("Pilkute")
print(sample_dict)

# Get specific data from dictionary
print(sample_dict['family'])
print(sample_dict.get('city'))
print(sample_dict.get('food', 'DefaultValue'))

# Deleting values form dictionary
del sample_dict['favorite_color']
deleted_value = sample_dict.pop('family')
print(deleted_value, 'was deleted')

print(json.dumps(sample_dict, indent=2))
