class Employee:
    # hidden data number or private member of employee class
    __Salary = 100000


e1 = Employee()
# print(e1.__Salary) -- This is not a right way of accessing hidden private variable.
# Access private hidden variable by using tricky syntax
print(e1._Employee__Salary)