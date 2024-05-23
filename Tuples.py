# Tuple is a collection of elements of any python data type
# Tuple vs List
# We have to store the values in a tuple with (), but in List: []
# Tuple is immutable but List is mutable so can not change the value of tuple elements

names = ("Java", "Dot Net", "Python", "C Sharp")
marks = (100, 200, 3000)
employeeData = ("Tommy", 25, "Male", 100000, True)

print(employeeData)

print(employeeData[0])
print(employeeData[3])
# print(employeeData[5]) # Tuple index out of range

print(employeeData[-1])
print(employeeData[-5])

listitems = [10, 20, 30, 40, 50]
listitems[1] = 100
print(listitems)

# Tuple is mutable not to support assignment
# names[2] = "English"
# print(names)

# Delete the tuple object
# del names
# print(names)

t1 = (1, 2, 3)
t2 = (4, 5, 6)

print(t1 + t2)

t3 = (7, 8, 9)
print(t3 * 3)

# Range Slicing
t4 = (1,2,3,4,5,6,7)
print(t4[1:3])

# in :
employeeData1 = ("Tommy", 25, "Male", 100000, True)
print(225 in employeeData1)

# Not in:
print(35 not in employeeData1)

# len:
length = len(employeeData1)
print(length)

# Max Number
number = (10,11,12,13,14,15)
print(max(number))

languages = ("Java", "Dot Net", "Python", "C Sharp")

print(max(languages))
print(min(languages))