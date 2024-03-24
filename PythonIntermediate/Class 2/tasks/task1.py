import json

with open('data.json') as in_file:
    data = json.load(in_file)

right_side = round(sum(data['right_side']) / len(data['right_side']), 2)
left_side = round(sum(data['left_side']) / len(data['left_side']), 2)

print("Right side", right_side)
print("Left side", left_side)
print("Average or Averages", (right_side + left_side) / 2)
