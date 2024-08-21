class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag=imag

    def __add__(self,other):
        return (f"{self.real + other.real} + {self.imag + other.imag }i")

a=Complex(12,25)
b=Complex(15,35)
print(a+b)

