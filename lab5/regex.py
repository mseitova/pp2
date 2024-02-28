import re
#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

# 1
s = str(input())
p = re.compile('a[b]*') 
m = p.search(s)
print(m)

# 2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

s = str(input())
p = re.compile('ab{3}|ab{2}')
m = p.search(s)
print(m)

# 3 Write a Python program to find sequences of lowercase letters joined with a underscore.
s = str(input())
p = re.compile('^[a-z]+_[a-z]+$')
m = p.search(s)
print(m)

# 4 Write a Python program to find the sequences of one upper case letter followed by lower case letters
s = str(input())
p = re.compile('[A-Z][a-z]+')
m = p.search(s)
print(m)

# 5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
s = str(input())
p = re.compile('a.*?b$')
m = p.search(s)
print(m)

# 6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.
s = str(input())
p = re.sub("[ ,.]", ":", s)
print(p)

# 7 Write a python program to convert snake case string to camel case string.
s = str(input())
words = s.split('_')
camel = words[0] + ''.join(word.capitalize() for word in words[1:])
print(camel)

# 8 Write a Python program to split a string at uppercase letters.
s = str(input())
p = re.findall("[A-Z][^A-Z]*", s)
print(p)

# 9 Write a Python program to insert spaces between words starting with capital letters.
s = str(input())
p = re.findall("[A-Z][^A-Z]*", s)
print(*p)

# 10 Write a Python program to convert a given camel case string to snake case.
s = str(input())
p = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
m = re.sub('([a-z0-9])([A-Z])', r'\1_\2', p).lower()
print(m)