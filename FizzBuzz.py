print("""if given number is divisible by
        3 & 5 = FizzBuzz!!
        only 3 = Fizz!!
        only 5 =Buzz!!""")

num=int(input("enter any number : "))
if num%3==0:
    if num%5==0:
        print("FizzBuzz!!")
    else:
        print("Fizz")
elif num%5==0:
    print("Buzz!!")
else:
    print("Sorr!! a given number is not Divisible by both 3 & 5 ")