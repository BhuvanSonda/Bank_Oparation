def factorial(x):
    fact = 1

    print("Factorial of numbers :\nnum = factorial ")
    while x >= 1:
        
        fact = 1
        for y in range(1, x + 1):
            # y+=1
            fact *= y

        print(x, '=', fact)
        x -= 1

factorial("6")