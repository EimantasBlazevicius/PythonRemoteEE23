import text_manipulation


def test_swap_case(text):
    assert text_manipulation.swap_case(text) == "qwe QWE ASD i"


def test_shortest_word(text):
    assert text_manipulation.shortest_word(text) == "I"
