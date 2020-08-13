# Strings are unmutable

# Slicing
str = 'Hello world'     # H e l l o   w o r l d
# str[start,pseudo-end]   0 1 2 3 4 5 6 7 8 9 10
print(str[0:5])
print(str[6:11])
print(str[:4])
print(str[7:])
print(str[6])
print(str[:])
print(str[:-1])
print('END')

# Concatenation
a = 'Hey'
b = a + 'there'
print(b)
c = a + ' ' + 'there'
print(c)
print('END')

# String Library

greet = 'Hello Guddu'

# lower()
print(greet.lower())
print('Guddu'.lower())

# find()
print(greet.find('u'))
print(greet.find('z'))

# replace()
print(greet.replace('Guddu','Surabhi'))

# Stripping - removing whitespaces
# .lstrip(), .rstrip(), strip()

# Prefixes
# .startswith() - gives boolean output
print('END')

line = 'forever'
print(type(line))
print(dir(str))

# Parsing & Extracting    **IMP**
data = 'surabhi.pmore@gmail.com October 12'
a = data.find(' ')
date = data[a+1:]
print(date)

