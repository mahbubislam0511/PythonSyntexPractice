class Car:
    # Class Variables
    wheels = 4

    # Constructor of this class
    # Default Constructor
    def __init__(self):
        print("Default Constructor")

    # Parameterized Constructor
    # overloading is not possible in python like other language & just take the latest one.
    def __init__(self, color):
        print("Car Class Constructor")
        self.color = color

    def test(self):
        print("Test Car Method")

    # If any var is declared inside the method or constructor : instance variable
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price


# How to create an object of this class:

C1 = Car("Red")
print(C1.wheels)
print(Car.wheels)

C1.test()
C1.setPrice(1000)
print(C1.getPrice())

C2 = Car("Black")
C2.setPrice(3000)
print(C2.getPrice())


class TestClass:
    a = 25


# Blank Class
class Pop:
    pass


P1 = Pop()
