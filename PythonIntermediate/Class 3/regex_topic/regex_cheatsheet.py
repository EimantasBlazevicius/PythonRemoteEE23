import re

# Base for Cheatsheet
play_string = '''abcdefghijklmnopqurtuvwxyz
abcDefghijklmNopqurtuvwxyZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
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

patternText = re.compile(r'ac')  # Exact text
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

patternListOfOptions = re.compile(r'')

result = re.findall(patterEndWithString, play_string)
print(result)
