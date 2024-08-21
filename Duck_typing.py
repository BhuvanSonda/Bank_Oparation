class cat:
    def legs(self):
        print("i am cat i have 4 legs ")
    def food(self):
        print("i eat both veg and non-veg\n ")

class cow:
    def legs(self):
        print("i am cow i have 4 legs ")
    def food(self):
        print("i eat herbs\n ")

class snake:
    def legs(self):
        print("i am snake i have no legs ")
    def food(self):
        print("i eat mouse ")

def display(self):
    self.legs()
    self.food()

c=cat()
co=cow()
s=snake()
display(c)
display(co)
display(s)