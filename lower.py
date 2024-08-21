from abc import ABC,abstractmethod
class vehicle(ABC):                 #abstract class
    @abstractmethod
    def medium(self):               #abstract method
        pass
    #@abstractmethod
    # def show(self):
    #     pass



    #concrete class
class Ship(vehicle):
    def medium(self):
        print("Water medium ")
class Train(vehicle):
    def medium(self):
        print("railway medium")
class Bus(vehicle):
    def medium(self):
        print("road medium")

v=Ship()
v.medium()
