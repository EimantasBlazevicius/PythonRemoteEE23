import csv

with open('csv_source.csv', 'r') as file:
    data = [row for row in csv.DictReader(file)]

with open('csv_output.csv', 'w', newline='') as output:
    headers = data[0].keys()
    writer = csv.DictWriter(output, fieldnames=headers)

    writer.writeheader()
    writer.writerows(data)
