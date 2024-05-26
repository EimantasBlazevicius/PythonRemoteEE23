def fibonacci_rec(n):
    print("Happens")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


#
# for number in range(1, 60):
#     print(number, fibonacci_rec(number))
fibonacci_rec(10)
