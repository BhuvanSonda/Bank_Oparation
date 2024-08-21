import random
name=['bhuvan','santoshi','rakshita']
print(f"guess the correct name from this list {name}")
a=random.choice(name)
gues=input("enter name ")
if gues==a:
    print(" your guessing is correct")
    print(f"the correct name is {a}")
elif gues not in name:
    print("You are out of range !! please enter valid name ")
else:
    print("You guessed wrong !!")
    print(f"the correct name is {a}")
