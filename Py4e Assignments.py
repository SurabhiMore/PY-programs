# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.
# GROSS PAY

hrs = input("Enter hours worked: ")
rate = input("Enter rate per hr: ")
if float(hrs) <= 40:
    pay = float(hrs) * float(rate)
    print(pay)
else:
    pay = (40 * float(rate)) + ((float(hrs) - 40) * float(rate) * 1.5)
    print(pay)
print('END')

# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

# (* Without try & except)

score = input("Enter score: ")
scr = 0.0 <= float(score) <= 1.0
if scr == True:
    if float(score) >= 0.9:
        print("A")
    elif float(score) >= 0.8:
        print("B")
    elif float(score) >= 0.7:
        print("C")
    elif float(score) >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Error : Score out of range")
print('END')

# 4.Gross Pay in Function
def computepay(h,r):
    if float(h) <= 40:
        return float(h) * float(r)
    else:
        return (40 * float(r)) + ((float(h) - 40) * float(r) * 1.5)
p = computepay((input("Enter hours: ")),(input("Enter rate: ")))
print("Pay",p)
print('END')

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

list = []
count = int(input('Enter count: '))   # no need of break statement (fixed input)
for n in range(count):
    numbers = input('Enter number: ')
    try:
        no = int(numbers)
    except:
        print('Invalid input')
    list.append(no)
lrgst = 0
for num in list:
    if num > lrgst:
        lrgst = num
print('Maximum is', lrgst)
smallest = 100
for i in list:
    if i < smallest:
        smallest = i
print('Minimum is', smallest)

# OR

# mast!
l = []
while True:
    numbers = input('Enter number : ')
    if numbers == 'done':
        break
    try:
        no = int(numbers)
        l.append(no)
    except:
        print('Invalid input')
lrgst = 0
for n in l:
    if n > lrgst:
        lrgst = n
print('Maximum is', lrgst)
smallest = None
for i in l:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
print('Minimum is', smallest)
print('END')

# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
a = text.find(':')    # gives the index of :
number = text[a+4:]   # slicing
print(float(number))
print('END')

# ************************************IMP*********************************************
# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

fname = input('Enter file name : ')  # mbox
fread = open(fname)
total = 0
count = 0
for line in fread:
   if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        a = line.find(':')
        b = line[a+1:]
        total += float(b)
        avg = total/count
print('Average spam confidence:',avg)
print('END')

# 8.4 Open the file and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

fh = open('py4e_lists')
lst = []
for line in fh:
    line = line.rstrip().split()
    for word in line:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
print('END')

# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

fread = open('mbox')
count = 0
for line in fread:
    words = line.rstrip().split()
    if len(words) < 3 or words[0] != 'From':   # NEW
        continue
    count += 1
    print(words[1])
print('There were', count, 'lines in the file with From as the first word')
print('END')

# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

lst = []
fh = open('mbox')
for line in fh:
    words = line.rstrip().split()
    if len(words) < 3 or words[0] != 'From':
        continue
    lst.append(words[1])
d = dict()
for prsn in lst:
    d[prsn] = d.get(prsn,0) + 1  # ***IMP***
person = None
bigcount = None
for name,count in d.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        person = name
print(person,bigcount)
print('END')

# TUPLES:
# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour

lst = []
fh = open('mbox')
for line in fh:
    words = line.split()
    if len(line) < 3 or words[0] != 'From':
        continue
    time = words[5]
    reqt = time.split(':')
    lst.append(reqt[0])
d = dict()
for hr in lst:
    d[hr] = d.get(hr, 0) + 1
sort_lst = sorted(d.items())
for k, v in sort_lst:
    print(k, v)
print('END')

# 11.Assignment
import re
lst = []
fh = open('regex_actual')
for l in fh:
    l = l.rstrip()
    num = re.findall('[0-9]+',l)
    if len(num) < 1:
       continue
    for n in num:
        if n in lst:
            continue
        else:
            lst.append(int(n))
print(sum(lst))
print('END')
# ***OR***
l = []
h = open('regex_actual')
for i in h:
    lt = re.findall("[0-9]",i)
    for v in lt:
        l.append(int(v))
print(sum(l))

# 12.1 Assignment
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
import re
# Retrieve all of the tags
lst = []
tags = soup('span')
for tag in tags:
    num = re.findall('[0-9]+',tag.decode())
    for n in num:
        if n in lst:
            continue
        else:
            lst.append(int(n))
print(sum(lst))
print('END')

# 12.2 Assignment chu..........
from bs4 import BeautifulSoup
import urllib.request
url = input('Enter URL:')
cunt = int(input('Enter count:'))
post = int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
href = soup('a')
for i in range(cunt):
    link = href[post].get('href')
    print (href[post].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')

# 13.1 Assignment
import urllib.request
url = input('Enter url: ')
info = urllib.request.urlopen(url).read()
import xml.etree.ElementTree as ET
stuff = ET.fromstring(info)
lst = stuff.findall('comments/comment')
total = 0
for item in lst:
    num = item.find('count').text
    total += int(num)
print(total)

# 13.2 Assignment
import urllib.request
url = input('Enter url: ')
data = urllib.request.urlopen(url).read()
import json
info = json.loads(data)
total = 0
for item in info['comments']:
    num = item['count']
    total += num
print(total)

# 13.3 Assignment
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure To Retrieve')
        continue

    print(js['results'][0]['place_id'])