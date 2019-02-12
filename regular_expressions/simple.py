import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'[\d]{3}[-.*]([\d]{3})[-.*]([\d])*' ) # matches  321-555-4321 similar phone no.
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*' )
matches = pattern.finditer(text_to_search)

for match in matches:
        print(match)


pattern1 = re.compile(r'Start')
pattern2= re.compile(r'sentence')
pattern3= re.compile(r'sentence')

matcher = pattern1.match(sentence)# only searches the beginning of the whole string, if not found returns null
print(matcher)


matcher = pattern2.match(sentence)# NONE bcz it is not beg of string
print(matcher)

matcher = pattern3.search(sentence) # it will search  even in middle of the string
print(matcher)


# Ignore case flag

pattern = re.compile(r'start', re.IGNORECASE) # event searches Upper case while here 's' is in lower case
matcher = pattern.search(sentence)
print(matcher)


















#
# with open('./data.txt', encoding='utf-8') as f:
#     contents = f.read()
#
# pattern = re.compile(r'')
# matches = pattern.finditer(text_to_search)
