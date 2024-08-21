a=0
b=1
sum=0
x=int(input("enter x value : "))
for i in range(x):
    a=b
    b=sum
    sum=a+b
    print(sum)


import string
lower=list(string.ascii_lowercase)

for i in range(1,x+2):
    strin=""
    for j in range(1,i):
        if i ==j:
            break
        else:
            strin+=lower[j-1]+" "
    print(strin)