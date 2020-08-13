# while loop - indeterminate loop
# while loop doesn't initialize the index hence it needs to be initialized explicitly

total = 0
j = 1
while j < 5:
    total += j
    j += 1
print("Total of numbers 1 to 4:",total)

# Addition of positive numbers
l = [4,5,3,2]
total = 0
i = 0
while i < len(l) and l[i] > 0:  # imp
    total += l[i]
    i += 1
print("Total :",total)

# for list in descending order only
# Type 1
l = [4,5,3,2,-1,-2]
total = 0
i = 0
while l[i] > 0:
    total += l[i]
    i += 1
print("Total :",total)

# For list in descending order only
# using Break statement
# Type 2
l = [4,5,3,2,-1,-2]
total = 0
i = 0
while True:
    total += l[i]
    i += 1
    if l[i] <= 0:
        break
print("Total :",total)

n = 5
while n > 0:
    print(n)   # 5,4,3,2,1
    n = n - 1
print("done")
print(n)       # last value i.e. 0 *****


# Using break statement
while True:
    line = input("Type something : ")
    if line == "done":
        break
    print(line)
print("Done!")

# Using continue & break statement
# IMP
while True:
    l = input("Type something - ")
    if l[0] == "#":
        continue
    if l == "done":
        break
    print(l)
print("Done!")

fruit = 'grape'
index = 0
# IMP
while index < len(fruit):
    letter = fruit[index]
    index += 1
    print(letter)


