class University(object):
    def karnataka(self):
        print("University : Karnataka University ")
    def kuvempu(self):
        print("University : Kuvempu University ")

class Course(University):
    def Engineering(self):
        print(" Course :Engineering Course ")
    def Agricultural(self):
        print(" Course : Agricultural Course ")
    def Medical(self):
        print(" Course : Medical Course ")

class Branches(University):
    def CS(self):
        print("Branch : CS ")
    def EC(self):
        print("Branch : EC ")
    def Mechanical(self):
        print("Branch : Mechanical ")
    def Horticulture(self):
        print("Branch : Horticulture ")
    def Forestry(self):
        print("Branch : Forestry ")
    def D_Pharm(self):
        print("Branch : D-Pharm ")
    def Nursing(self):
        print("Branch : BSc Nursing ")
class Student(Course,Branches):
    def Name(self,name):
        self.Name=name
        print('Student Name : ',self.Name)

class Faculty(Branches):
    def Name(self,name):
        self.name=name
        print('Faculty Name :',self.name)
s=Student()
s.Name('Bhuvan')
s.karnataka()
s.Medical()
s.D_Pharm()
print('\n')
f=Faculty()
f.Name('kavya')
f.CS()
f.karnataka()