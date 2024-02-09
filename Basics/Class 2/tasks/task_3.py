# Write a program that would ask user to input text split the received text in half and print first part normally and a second part reversed to output.
text = input("Enter some text to be reformatted: ")
half_index = int(len(text)/2)
first_half = text[:half_index]
second_half = text[half_index:]
print(f"this is the reformatted version: {first_half}{second_half[::-1]}")