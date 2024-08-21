class Animal:
    def survive(self):
        print("it can survive in zoo ")
class herbivorous(Animal):
    def food(self):
        print("it eats  plants ")
class carnivorous(Animal):
    def Food(self):
        print("it eats  meat ")
class omnivorous(herbivorous,carnivorous):
    def eat(self):
        (herbivorous.food(self))
        (carnivorous.Food(self))
        #(Animal.survive(self))
        print("it eats both meat and plants ")
f=omnivorous()
f.eat()
f.survive()
