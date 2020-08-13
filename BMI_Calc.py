# BMI Calculator :-
# if elif else

# person details
weight = int(input("Enter weight in kg : "))
height = float(input("Enter height in m : "))
print("Weight : ", weight)
print("Height : ",height)
# bmi formula
bmi = weight / (height ** 2)
print("BMI : ",bmi)
# result
if bmi < 18:
    print("Underweight")
elif bmi > 25:
    print("Overweight")
else:
    print("Normal")