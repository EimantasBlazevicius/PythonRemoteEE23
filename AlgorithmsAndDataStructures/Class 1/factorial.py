def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# def rec_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

def rec_factorial(n, memory={0: 1, 1: 1}):
    if n in memory:
        return memory[n]
    else:
        memory[n] = n * factorial(n - 1)
        return memory[n]


print(rec_factorial(100))
