def check(a,b=36):
    print("a=",a)
    print("b=", b)
def num(a,b):
    print("a=",a)
    print("b=",b)

check(12,25)
num(b=15,a=36)

def arb(*tuple):
    print(tuple)

arb(1,5,2,4,3,6)
num=[1,45,23,58]
arb(num)

def key(**dict):
    print(dict)

key(name='bhuvan',age=20,id=1243)

