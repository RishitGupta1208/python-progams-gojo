x=float(input("please enter your height in cm:"))
y=float(input("please enter your weight in kg:"))
z=y/(x/100)**2
print("your BMI is",z)
if z<=16.2:
    print("you are severly underweight")
elif z<=18.4:
    print("you are underweight")
elif z<=24.9:
    print("you are healthy")
elif z<=29.9:
    print("you are overweight")
else:
    print("you are obese")