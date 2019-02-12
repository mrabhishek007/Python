import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'(http[s]?://)(www\.)?(\w+)(\.[a-z]+)')

# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)

matches = pattern.finditer(urls)  # recommended to use

# matches = pattern.findall(urls) # only returns a tuple of group



for match in matches:
    print(match.group()) # group 0 prints the whole founded text
    print(f'{match.group(1)},  {match.group(2)}, {match.group(3)}   ')


# shorthand for printing group name
sub_url = pattern.sub(r'\2\3', urls)
print(sub_url)

