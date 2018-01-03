import re

text = '''Who is the value of parameter ?
and of course why google is called google'''

type = re.findall(r'goo[a-z]*',text)
print(type)

