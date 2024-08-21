class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

p1=Person('ram',20)
p2=Person('shashi',30)

if p1>p2:
    print(f"{p1.name} pay the bill")
else:
    print(f"{p2.name} pay the bill")