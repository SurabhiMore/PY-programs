# (Regex)
# re.search() ~ find() in string

import re
fh = open('mbox')
for line in fh:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
print('DONE!')

# re.findall() ~ combn. of find() & slicing (returns a list)

import re
str = 'My 2 favourite numbers are 2 and 12.'
x = re.findall('[0-9]+', str)    # to find numbers in string
print(x)
y = re.findall('[aeiouAEIOU]+', str)  # to find vowels in string
print(y)
print('DONE!')

import re
# Greedy
s = 'From: Using the: character'
x = re.findall('^F.+:', s)  # till the first colon
print(x)
# Non-Greedy
y = re.findall('^F.+?:', s) # till the last colon
print(y)
print('Done!')

import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
x = re.findall('\S+@\S+', line)
print(x)
y = re.findall('@([^ ]*)', line)
print(y)



