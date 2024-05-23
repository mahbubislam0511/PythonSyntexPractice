class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):

    # overridden Method
    def isEmployee(self):
        return True


# Test Person Class
emp = Person("Mahbub")
print(emp.name)
print(emp.getName(), emp.isEmployee())

emp1 = Employee("Tommy")
print(emp1.name)
print(emp1.getName())
print(emp1.isEmployee())