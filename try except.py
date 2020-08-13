# to avoid getting Traceback
a = input("Enter a value: ")
try:
    val = int(a)
except:
    val = -1
if val > 0:
    print('Good job!')
else:
    print("Not a number or not greater than 0")


