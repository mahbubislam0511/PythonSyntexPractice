class Base1(object):
    def __init__(self):
        self.str1 = "Mahbub"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Salam"
        print("Base2")


class Child(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

        print("Child Class")

    def printStringsValue(self):
        print(self.str1, self.str2)


ob = Child()
ob.printStringsValue()

