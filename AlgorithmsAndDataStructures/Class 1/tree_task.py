from tree import items_table


def print_name_rec(item, sep="-"):
    print(f"{sep} {item['name']}")
    if len(item['children']):
        for child in item['children']:
            print_name_rec(child, sep=f"{sep} -")


for item in items_table:
    print_name_rec(item)
