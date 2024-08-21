class human:
    def eat(self):
        print("i can eat ")
class male():
    def __init__(self,name):
        self.name=name
    def work(self):
        print("i can work")

# boy=male('bhuvan')
# boy.eat()
# print(boy.name)

class Boy(human,male):
    def work(self):
        male.work(Boy)
        print("i can sleep")

chk=Boy('bhuvan')
chk.work()