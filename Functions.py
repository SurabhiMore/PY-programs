# Using return statement (uses variable)

def convert(miles):
    return 1.6 * miles
km = convert(int(input("Enter distance in miles : ")))
print("km :",km)


def function(x):
    print("x = ",x)
    print("Still in function")
    return x ** 2
b = function(int(input("Enter number : ")))
print("sqr =",b)










