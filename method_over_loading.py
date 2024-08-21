class Addition:
    def add(self,*args):
        sum = 0
        for i in args:
            sum += i
        return sum
        
a=Addition()
print(a.add(1,2,3,4,5,6,7,8))
print(a.add(12,3,10))

class maths:
    def add(self,a,b,c=0):
        return a+b+c
A=maths()
print(A.add(1,2))