def binary_iter(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    steps = 0

    while low <= high:
        steps += 1
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def binary_rec(arr, x, high, low=0):
    if low <= high:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_rec(arr, x, mid - 1, low)
        else:
            return binary_rec(arr, x, high, mid + 1)
    else:
        return -1


pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
the_page = 12

print(binary_iter(pages, the_page))
print(binary_rec(pages, the_page, high=(len(pages) + 1)))
