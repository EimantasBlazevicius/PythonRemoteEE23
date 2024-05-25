print("Hello world")
print()


def square():
    a = input("Give me a number")
    p = a * a
    return p


def password_check():
    password = ""
    while password != "854":
        password = input("Read Code")
    print("code accepted")


def dec_to_bin():
    binary_string = ""
    d = -1
    while d < 0:
        d = int(input("Enter the integer number"))

    while d != 0:
        r = d % 2
        if r == 1:
            binary_string = f"1{binary_string}"
        else:
            binary_string = f"0{binary_string}"
        d = d // 2

    return binary_string


print(dec_to_bin())


def gcd():
    a = int(input("Input A"))
    b = int(input("Input B"))

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
