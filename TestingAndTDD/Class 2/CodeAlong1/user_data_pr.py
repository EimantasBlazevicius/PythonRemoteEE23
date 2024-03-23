def prepare_data(file):
    headers = file.readline().strip().split(",")
    content = file.readlines()
    result_list = []
    for line in content:
        record = line.strip().split(",")
        content_with_headers = {}
        for index, value in enumerate(record):
            content_with_headers[headers[index]] = value
        result_list.append(content_with_headers)

    return result_list


def filter_underage(people_list):
    for index, person in enumerate(people_list):
        if int(person['age']) < 18:
            people_list.pop(index)

    return people_list


with open("../../../PythonIntermediate/Class 1/csv_source.csv", "r") as f:
    print(prepare_data(f))
