def is_anagrams(first, second):
    if sorted(first) == sorted(second):
        return True
    return False


text1 = input("Enter the first word: ")
text2 = input("Enter the second word: ")

if is_anagrams(text1, text2):
    print("These words are anagrams")
else:
    print("These words are not anagrams")
