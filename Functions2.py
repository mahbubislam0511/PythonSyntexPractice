def login(username, password):
    print(username, password)


login("mahbub", "test123")

login(username="mahbub", password="test123")


# *arg
def getMarks(*arg):
    for x in arg:
        print(x)


getMarks(10, 20, 30, 40, 50)

getMarks("A", "A+", "B", "B+", "C")


# Keywords args
# **arg
def getStudentMarks(**args):
    for key, value in args.items():
        print("%s == %s" % (key, value))


getStudentMarks(navenn=10, Tom=20, Sijan=80)
getStudentMarks(fruit="Apple", seller="Mahbub")

# Lambda functions : Anonymous function
# A fun without any name:

cube = lambda x: x * x * x
print(cube(4))

total = lambda marks: marks + 30
print(total(100))
