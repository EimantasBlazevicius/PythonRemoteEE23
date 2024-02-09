# Write a program that would ask user to input text and print the amount of times the first character of user entered text is repeated.
text = input("Enter the text and I will let you know how may characters match the first one: ")
print(f"The amount of {text[0]} in the provided text is: {text.count(text[0])}")