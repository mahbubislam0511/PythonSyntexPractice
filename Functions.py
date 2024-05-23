# Zero parameterized function
def test():
    print("Hello World")


test()


# parameterized function
def summation(a):
    print(a + 10)


summation(50)


# optional/Default Parameter
def getCountryName(name="india"):
    print(name)


getCountryName()
getCountryName("UK")


# Pass a list to function
def getNames(namelist):
    for i in namelist:
        print(i)


names = ["Java", "Python", "C", "Ruby"]
getNames(names)


# Functions with return
def summation2(a, b):
    return a + b


c = summation2(100, 500)
print(c)


# Functions with If Else conditions
def launchBrowser(browsername):
    if browsername == "chrome":
        print("Launch Google Chrome")
    elif browsername == "firefox":
        print("Launch Firefox")
    else:
        print("No Browser is defined")


launchBrowser("chrome")


# Recursion in Python
# A func is calling itself

# Write a program to get the factorial of a given number
# fact(4) = 4*3*2*1 = 24
# fact(5) = 5*4*3*2*1 = 120

def fact(num):
    if num > 1:
        num = num * fact(num - 1)
    return num


print(fact(4))
