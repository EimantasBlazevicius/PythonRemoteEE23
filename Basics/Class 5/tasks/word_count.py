import json

text = "Cupcake ipsum dolor sit amet croissant. Lemon drops biscuit shortbread tootsie roll pie. Muffin sweet roll gummies pudding chocolate chocolate cake I love cotton candy. I love jelly caramels bonbon icing. Cookie bonbon dessert powder bonbon fruitcake. Muffin chocolate cake chocolate cake jelly-o biscuit. Gummies brownie gingerbread dessert powder. Dragée macaroon soufflé pastry powder. Oat cake cake gingerbread I love marzipan cake chupa chups cake. Candy tootsie roll brownie pie chocolate bar toffee jelly-o liquorice. Sweet gingerbread chocolate bar cheesecake cake chocolate bar. Topping ice cream biscuit apple pie donut cupcake wafer gummies caramels. Lemon drops shortbread sweet lollipop donut apple pie. Gingerbread candy canes donut jelly-o jelly-o icing brownie. Chocolate bar jelly beans sesame snaps donut carrot cake bonbon danish gummies. Sugar plum marzipan lemon drops apple pie pastry soufflé sweet. Fruitcake lollipop cheesecake shortbread I love. Cake marshmallow jujubes I love icing liquorice. Liquorice powder marshmallow I love dessert bonbon lemon drops. Carrot cake marshmallow halvah I love bear claw. Gingerbread tart donut I love I love. Croissant gummies I love candy canes marshmallow cake halvah jelly-o lemon drops. Chocolate bar bear claw I love I love dessert topping lollipop tiramisu. Candy canes liquorice jujubes gingerbread lemon drops pastry topping croissant. Topping chupa chups bonbon cookie apple pie. Tootsie roll pie liquorice jelly beans I love jujubes."
words_counter = {}

words_list = text.split()

for word in words_list:
    if words_counter.get(word.strip(".")):
        words_counter[word.strip(".")] += 1
        print("In")
    else:
        words_counter[word.strip(".")] = 1
        print("Not in")

print(json.dumps(words_counter, indent=2))
