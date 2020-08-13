# swapping variables
a = 1
b = 2
temp = a
a = b
b = temp
print("a = ",a)
print("b = ",b)
#hello



























































































#NotWorking
numArray = map(int, input().split()) # Get the input
sum_integer = 0
# write your logic to add these 4 numbers here
for num in numArray:
    sum_integer += num
print(sum_integer) # Print the sum
#next
# Get L and R from the input
L, R = map(int, input().split())
# Write here the logic to print all integers between L and R
for i in range(L,R+1):
    print(i, end= " ")
print(" ")
#next
N = int(input())
# Get the array
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))
sumArray = []
# Write the logic here:
for i in range(0, N):
    sumArray.append(numArray1[i] + numArray2[i])
# Print the sumArray
for element in sumArray:
    print(element, end=" ")
print("")