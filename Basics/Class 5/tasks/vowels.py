vowels = 'aeiou'
text = "Cupcake ipsum dolor sit amet chocolate bar apple pie I love. I love marshmallow gummies I love jujubes candy canes. I love I love chocolate I love cupcake oat cake gingerbread."
amount_of_vowels = 0

for char in text:
    if char.lower() in vowels:
        amount_of_vowels += 1

print(f"Number of vowels in the text: {amount_of_vowels}")
