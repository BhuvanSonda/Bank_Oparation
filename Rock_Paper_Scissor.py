import random

objects = ['rock','paper','scissor',]
print(objects)
own=0
lost=0
draw=0
k=1
while (k):
    k= int(input("for exit enter 0 else enter 1 : "))
    if k == 0:
        break

    choice = input("choose any one : ").lower()
    c_choice = random.choice(objects)
    if choice == c_choice:
        draw+=1
        print("Draw match!!")
    elif choice == 'rock' and c_choice == 'paper':
        lost+=1
        print("You lost the match !!")
    elif choice == 'rock' and c_choice == 'scissor':
        own+= 1
        print("You own the match !!")
    elif choice == 'paper' and c_choice == 'scissor':
        lost += 1
        print("You lost the match !!")
    elif choice == 'paper' and c_choice == 'rock':
        own += 1
        print("You own the match !!")
    elif choice == 'scissor' and c_choice == 'paper':
        own += 1
        print("You own the match !!")
    elif choice == 'scissor' and c_choice == 'rock':
        lost += 1
        print("You lost the match !!")
    else:
        print("you enter wrong value")
    print(f"computer choose {c_choice}")

print(f"\nyour score = {own} \ncomputer score = {lost}\ndraw match ={draw}")
