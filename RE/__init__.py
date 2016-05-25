import re

# match
m1 = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(m1)

# not match
m2 = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print(m2)
print(re.split(r'\s+', 'a b   c'))
