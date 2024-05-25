import sys

sys.setrecursionlimit(999999)


# integer = 0
# while True:
#     integer += 1
#     print(f"Potato {integer}")

# def recursive(a):
#     if a == 1:
#         return 1
#     else:
#         recursive(a - 1)
#
#
# recursive(9)

def inf_rec(number):
    if number != 0:
        inf_rec(number)
    return 0


inf_rec(5)
