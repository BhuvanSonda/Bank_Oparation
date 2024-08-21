def variable(name):
    print("your name length of your name : ",len(name))

#name=input("enter your name to find length")
#variable(name)

def outer(a,b):
    sum=0

    def inner(a,b):
        return a+b
    sum=inner(a,b)
    print("outer sum is :",sum+5)

outer(50,10)


def recursive(x):
    if x == 1:
        return x
    sum=x*recursive(x-1)
    return sum

print("value of recursive function : ",recursive(4))

def list(x):
    List=[]
    for i in range(4,x,2):
        List.append(i)
    return List


LIST=list(30)
print(LIST)

import random
LIST.extend([15,50,63,89,100,85])
random.shuffle(LIST)
def largest(LIST):
    print(LIST)
    large=0
    j = 0
    for i in LIST:

        if i > j:
            j=i
            large=j
        else:
            continue
    print("largest number in list is :",large)
largest(LIST)

names=['Bhuvan','ram','seeta']
age=[20,30,40]
bio=dict()
def dectionary():
    bio = dict(zip(names, age))
    print(bio)
dectionary()

def perfect(x):
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum+=i
    if sum == x:
        print("perfect number")
    else:
        print("not perfect number")

perfect(28)

x=5
for i in range(1,x):

    print("*  "*i)
