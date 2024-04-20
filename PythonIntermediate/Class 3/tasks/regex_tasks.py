import re

# task 1 and 1.1
the_string = "test43543lfdsfdsfl534543fdgl432fr"

task_one_pattern = re.compile(r'\d+')
resultSub = task_one_pattern.sub('', the_string)

result = task_one_pattern.findall(the_string)
# print(resultSub)

# task 2
phone_number_regex = re.compile(r'\+370[56]\d{7}')
phone_result = phone_number_regex.match('+37060482010')
print(phone_result)

# Extra tasks
# 1
pattern_text = re.compile(r'Say hello to the world')  # Exact text
# 2
pattern_match_any_number = re.compile(r'\d+')
# 3
text = "Contact us at email@example.com or support@example.org"
pattern_email = re.compile(r'\w+@\w*\.(com|org)')
# 4
text2 = "Apples are awesome and so are bananas"
pattern_words_starting_with_a = re.compile(r'\b(A|a)\w+')
# 5
text3 = "Visit us at http://example.com or https://www.example.org"
pattern_urls = re.compile(r'https?:\/\/(www\.)?\w+\.(org|com)')
