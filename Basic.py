# nos. divisible by 5 and less than 150
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for n in list1:
    if n>150: break
    if n%5 == 0:
        print(n)

# Reversing a list
list1 = [10, 20, 30, 40, 50]
list1.reverse()
print(list1)

# Pyramid
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print("\r")

# print function
num1 = int(input('Enter number: '))
num2 = int(input('Enter number: '))
add = num1 + num2
print("Sum of {0} and {1} is {2}" .format(num1, num2, add))
print('END')

# Prime number:
num = int(input('Enter number - '))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")
print('END')

# Armstrong Number:
# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153
l = []
num = input("Enter number: ")
count = 0
for n in num:
    count += 1
for dig in num:
    l.append(int(dig) ** count)
if int(num) == sum(l):
    print('Yes')
else:
    print('No')
print('END')

# Factorial of a number:
# Recursive:
def fact(n):
    return 1 if (n==1 or n==0) else n*fact(n-1)
n = int(input('Enter number: '))
print(fact(n))
#Loop:
def factorial(n):
    if n==0 and n==1:
        return 1
    else:
        fact = 1
        while n>1:
            fact = fact * n
            n = n -1
        return fact
n = int(input('Enter number: '))
print(factorial(n))
print('END')

# Simple interest:
def simple_interest(p,t,r):
    si = (p*t*r)/100
    return si
p = int(input('Enter principle: '))
t = int(input('Enter time peiod: '))
r = int(input('Enter rate of interest: '))
print(simple_interest(p,t,r))
# Compound interest = p(1 + r/100)**t
print('END')

# swapping variables
a = 1
b = 2
temp = a
a = b
b = temp
print("a = ",a)
print("b = ",b)




























































































