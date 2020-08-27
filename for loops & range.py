# for loop - determinate loop (having exact/observable limits)

fruit = input('Enter fruit name: ')
print('Letters in the fruit:-')
for letter in fruit:
    print(letter)
print('END')

fruit = input('Enter fruit name: ')
count = 0
for letter in fruit:
    if letter == 'a':
        count += 1
print("Number of 'a's in the fruit:", count)   # numbers of 'a's in the string

for i in [1,2,3]:
    print(i)
print("Po")

frnds = ['Milly','Silly','Lilly']
for frnd in frnds:
    print("Bonjour",frnd)
print("Done!")

# range(start,pseudo-end,skip)
for i in range(3,0,-1):   # IMP
    print(i)
print('END')

# compute all multiples of 3 & 5 that are less than 100
total = 0
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        total += i
print("Total of all the multiples of 3 & 5:",total)
print('END')

total = 0
for i in range(1,5):
    total += i
print("Addition of numbers 1 to 4:",total)
print('END')

# when we don't know the length & elements of list
l = ["hey","hello","hi"]
for i in range(len(l)):
    print(l[i])
# OR
for i in l:   # best alternative for above
    print(i)
print('END')

# for numbers before any negative number
# sum of positive integers = 19
l = [4,5,3,2,-1,-2,0,4,2]
total = 0
for i in l:
    if i <= 0:
        break
    total += i
print("Total :",total)
print('END')

# Finding largest number (max() function)
count = int(input('Count? '))
list = [int(input('Enter number: ')) for n in range(count)]
print('List :',list)
# imp
lrgst_so_far = 0
for num in list:
    if num > lrgst_so_far:
        lrgst_so_far = num
print('Largest number :',lrgst_so_far)
print('END')

# Finding smallest number (min() function)
count = int(input('Enter count = '))
numbers = [int(input("Enter value: ")) for no in range(count)]
print('Numbers :',numbers)
# imp
smallest = None
for value in numbers:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
print('Smallest number =',smallest)
print('END')

# Counting the number of iterations (8)
l = [3,4,23,34,54,66,6,2]
print('Iterations =',len(l))
print('END')

# Summing & Average in a loop
lst = [int(input('Enter number : ')) for n in range(int(input('Enter count : ')))] # using list comprehension
print('List :',lst)
sum = 0
for i in lst:  # without using the sum() function
    sum += i
print('Total =',sum)
avg = sum/count
print('Average =',avg)
print('END')

# Search using a variable & boolean
numbers = []     # without using the list comprehension
cnt = int(input('Enter count : '))
for i in range(cnt):
    numbers.append(int(input('Enter number : ')))
print('List :',numbers)
# IMP
found = False
search = int(input("Enter number to be searched : "))
for value in numbers:
    if value == search:
        found = True
print('Result :',found)
print('END')



