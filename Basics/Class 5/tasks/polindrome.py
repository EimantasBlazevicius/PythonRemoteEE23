def reverse_string(text):
    return text[::-1]


def is_palindrome(text):
    if text == reverse_string(text):
        print("It is a palindrome")
    else:
        print("Nah bra")


check_text = input("Check if this is palindrome: ")
is_palindrome(check_text)
