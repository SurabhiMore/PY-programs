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
# Greedy method
s = 'From: Using the: character'
x = re.findall('^F.+:', s)  # till the first colon
print(x)
# Non-Greedy method
y = re.findall('^F.+?:', s) # till the last colon
print(y)
print('Done!')

import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
x = re.findall('\S+@\S+', line)
print(x)
y = re.findall('@([^ ]*)', line)
print(y)




# ^ - Matches the beginning of the line.

# $ - Matches the end of the line.

# \s - Matches a whitespace character.

# \S - Matches a non-whitespace character (opposite of \s).

# * - Applies to the immediately preceding character(s) and indicates to match zero or more times.

# *? - Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”.

# + - Applies to the immediately preceding character(s) and indicates to match one or more times.

# +? - Applies to the immediately preceding character(s) and indicates to match one or more times in “non-greedy mode”.

# ? - Applies to the immediately preceding character(s) and indicates to match zero or one time.

# ?? - Applies to the immediately preceding character(s) and indicates to match zero or one time in “non-greedy mode”.

# [a-z0-9] - You can specify ranges of characters using the minus sign. This example is a single character that must be a lowercase letter or a digit.

# [^A-Za-z] - When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.

# ( ) - When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().

# \b - Matches the empty string, but only at the start or end of a word.

# \B - Matches the empty string, but not at the start or end of a word.

# \d - Matches any decimal digit; equivalent to the set [0-9].

# \D - Matches any non-digit character; equivalent to the set [^0-9].


