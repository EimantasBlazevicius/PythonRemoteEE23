def swap_case(text):
    char_list = []
    for char in text:
        if char.isupper():
            char_list.append(char.lower())
        else:
            char_list.append((char.upper()))

    return ''.join(char_list)


def shortest_word(text):
    shortest = ''
    length = 99

    words = text.strip().split(" ")
    for word in words:
        if len(word) < length:
            length = len(word)
            shortest = word

    return shortest
