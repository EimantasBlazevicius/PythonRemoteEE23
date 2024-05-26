sorting_list = [0, 3, 6, 9, 5, 4, 1, 2, 6, 55, 7, 9, 4, 33, 6, 9, 7, 141, 9, 96, 58, 1, 32, 3]


def bubble(sortable):
    indexing_length = len(sortable) - 1
    sorted = False
    while not sorted:
        sorted = True
        for index in range(0, indexing_length):
            if sortable[index] > sortable[index + 1]:
                sorted = False
                sortable[index], sortable[index + 1] = sortable[index + 1], sortable[index]
        print(sortable)
    return sortable


bubble(sorting_list)


def insertion(sortable):
    indexing_range = range(1, len(sortable))
    for index in indexing_range:
        value_to_sort = sortable[index]

        while sortable[index - 1] > value_to_sort and index > 0:
            sortable[index], sortable[index - 1] = sortable[index - 1], sortable[index]
            index -= 1
        print(sortable)
    return sortable


insertion(sorting_list)


def selection(sortable):
    indexing_range = range(0, len(sortable) - 1)

    for index in indexing_range:
        print(sortable)
        min_index = index
        for subIndex in range(index + 1, len(sortable)):
            if sortable[subIndex] < sortable[min_index]:
                min_index = subIndex

        if min_index != index:
            sortable[min_index], sortable[index] = sortable[index], sortable[min_index]

    return sortable


selection(sorting_list)


def quick(sortable):
    length = len(sortable)
    print(sortable)
    if length <= 1:
        return sortable
    else:
        pivot = sortable.pop(0)

        items_greater = []
        items_lower = []

        for item in sortable:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

    return quick(items_lower) + [pivot] + quick(items_greater)


quick(sorting_list)
