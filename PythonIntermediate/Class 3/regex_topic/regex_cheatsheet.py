import re

# Base for Cheatsheet
play_string = '''abcdefghijklmnopqurtuvwxyz
abcDefghijklmNopqurtuvwxyZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \\ | ( )
lietuva.com
ac
+37060482010
}37060482010
+370.604.82.010
+370-604-82-010
+aaa-604-82-010
+ddd-604-82-010
-37060482010
111.999.6699
eima.blaz@gmail.com_'''

pattern_text = re.compile(r'abcdefghijklmno')  # Exact text
patternAnyText = re.compile(r'.')  # Any text
patternDigits = re.compile(r'\d')  # All digits
patternNotDigits = re.compile(r'\D')  # All not digits
patterCharacters = re.compile(r'\w')  # Characters and _
patterNotCharacters = re.compile(r'\W')  # Not characters and not _
patternWhiteSpace = re.compile(r'\s')  # White space and new line
patternNotWhiteSpace = re.compile(r'\S')  # Not White space and new line

patternWordBoundary = re.compile(r'\bHa')  # Occurrences of Ha even if it is star of another work
patternNotWordBoundary = re.compile(r'\BHa')  # Individual occurrences of Ha
patternStartString = re.compile(r'^abc')  # Start with string
patterEndWithString = re.compile(r'.com_')  # Ends with String

patternListOfOptions = re.compile(r'[+-]37060482010')  # List of options
patternNotListOfOption = re.compile(r'[^+-]37060482010')  # Not list of options
patternGrouping = re.compile(r'\+(\d\d\d).(\d\d\d).(\d\d.\d\d)')  # Grouping
patternGroupingWithOr = re.compile(r'\+(\d\d\d|\w\w\w).(\d\d\d).(\d\d.\d\d)')  # Grouping with OR

patternZeroOrMore = re.compile(r'\+370*')  # Zero or more
patternOneOrMore = re.compile(r'\+370+')  # One or more
patternOptionalCharacter = re.compile(r'ab?c')  # Optional Character
patternExactNumber = re.compile(r'\+(\d{3}).(\d{3}).(\d{2}.\d{2})')
patternRangeOfNumbers = re.compile(r'(\d{3}).(\d{3}).(\d{2,4})')

result = re.findall(patternOneOrMore, play_string)
print(result)

#  Find first occurrence of the pattern in the text
resultSearch = patternText.search(play_string)
# print(resultSearch.group(0))

#  Match the start of the text
resultMatch = patternText.match(play_string)
# print(resultMatch)

#  Find all occurrences
resultFindAll = patternText.findall(play_string)
# print(resultFindAll)

# Same as find all but returns an iterator
resultFindAllIter = patternText.finditer(play_string)
# print(resultFindAllIter)

# Split functionality
resultSplit = patternWhiteSpace.split(play_string)
# print(resultSplit)

# Substitute with another
resultSub = patternWhiteSpace.sub('Potato', play_string)
# print(resultSub)

# Substitute with another but shows how many substitutes done
resultSubN = patternWhiteSpace.subn('Potato', play_string)
# print(resultSubN)
