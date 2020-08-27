# Urllib module - URL handling module for python

# Retrieving Web Pages

import urllib.request, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')  # similar to opening a file
count = dict()
for line in fhand:
    words = line.decode().split()  # returns list
    for word in words:
        count[word] = count.get(word,0) + 1  # inserting in the dictionary
print(count)
print('END')

fh = urllib.request.urlopen('http://data.pr4e.org/clown.txt')
for l in fh:
    print(l.strip().decode())
print('END')

# Parsing Web Pages - using BeautifulSoup library (HTML)

# BeautifulSoup - Python library for pulling data out of HTML and XML files

from bs4 import BeautifulSoup
html = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm').read()  # html in single line as a string
soup = BeautifulSoup(html, 'html.parser')  # returns html in clean & structured way
# Retrieve all of the anchor tags
tags = soup('a')  # returns list of anchor tags
for tag in tags:
    print(tag.get('href', None))  # href is an attribute

import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')            # https://www.si.umich.edu/
html = urllib.request.urlopen(url, context=ctx).read()  # UTF-8 string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')    # gives list of tags(here, anchor tags)
for tag in tags:
    print(tag.get('href', None))
