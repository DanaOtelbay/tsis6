#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

import re

s = 'The quick Brow Fox'

upper = re.findall(r"[A-Z]+", s)
lower = re.findall(r"[a-z]+", s)

upper_len = 0
lower_len = 0

for i in upper:
   upper_len += len(i)

for i in lower:
    lower_len += len(i)

print(upper_len)
print(lower_len)