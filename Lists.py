# Lists are mutable
# Concatenation and Slicing in Lists is same as in Strings

l = []
print(type(l))
print(dir(l))


# Methods of forming list

# by append function
a = list()
a.append(10)
a.append(20)
a.append(30)
a.append(40)
print(a)
# using 'in' & 'not in' operator
print(10 in a)
print(2 in a)
print(2 not in a)

b = []
for i in a:
    b.append(i * 2)
print(b)

# list comprehension
c = [x//2 for x in b]
print(c)

L = list()
for e in range(1,21):
    L.append(e)
print(L)

d = [i*2 for i in range(1,6)]
print(d)

l = list(range(1,5)) # using list function
print("list :",l)


# using while loop - Easy way  (more sophisticated)
num = []
while True:
    no = input('Enter no : ')
    if no == 'done':
        break
    try:                #to avoid Traceback
        n = int(no)
    except:
        print('Invalid input')
    num.append(n)
print('NumLst :',num)



# .sort() - sorts alphabetically
frnds = ['Milly','Silly','Lilly']
frnds.sort()
print(frnds)

# alternative for finding sum() & average of lists without for loop
lst = list(range(1,101))
print('List :',lst)
print('Maximum =',max(lst))
print('Minimum =',min(lst))
print('Sum =',sum(lst))
print('Length =',len(lst))
print('Average =',sum(lst)/len(lst))


# Swapping elements in list
# Method 1
list = [1, 2, 3]
temp = list[0]
list[0] = list[2]
list[2] = temp
print("swap_list : ",list)
# Method 2  BEST
l = list(range(1,100))
print("list : ",l)
l[0], l[-1] = l[-1], l[0]
print("swap_list : ",l)


