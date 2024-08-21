import random
coin=['H','T']
guess = input("what is you choice (Head = H / Tail = T) ").upper()
a = random.choice(coin)
if guess == a:
    print("You own Toss")
    print(f"Toss is {a}")
elif guess not in coin:
    print("enter only H or T")
else :
    print("You lose the Toss ")
    print(f"Toss is {a}")
