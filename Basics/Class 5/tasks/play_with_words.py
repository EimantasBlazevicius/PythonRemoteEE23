original_text = "Cupcake ipsum dolor sit amet. I love caramels topping soufflé I love"
final_string = ""

for index, char in enumerate(original_text):
    if (index + 1) % 3 == 0:
        final_string += char.upper()
    elif (index + 1) % 4 == 0:
        final_string += f"{char}!"
    else:
        final_string += char

print(final_string)
