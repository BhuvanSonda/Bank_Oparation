weight=float(input("entr weiht in kg "))
height=float(input("enter weight in foot / meter "))
unit=input("enter unit f/m ")
bmi=0
if unit in 'fF':
    height *= 0.3048
    bmi=weight/(height**2)
elif unit in 'mM':
    bmi = weight / (height ** 2)

else:
    print("Sorry.. You entered wrong unit!!")

print(f"Your BMI is {round(bmi,2)}")

if bmi<18:
    print("Your in Underweight")
elif bmi <25:
    print("Your in Normalweight")
else:
    print("Your in Overweight")