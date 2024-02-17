text = "Cupcake ipsum dolor sit amet chocolate bar apple pie I love. I love marshmallow gummies I love jujubes candy canes. I love I love chocolate I love cupcake oat cake gingerbread."


def modify(original):
    return original.replace(" ", "_").lower()


print(modify(text))
