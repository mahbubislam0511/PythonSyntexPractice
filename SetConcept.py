# Set - not order based

# It stores different types of data

# It performs different mathematical data types

# It does not stores duplicate elements

# Define a set : use {}

S1 = {"Tommy", 10, 15.5, True}

S2 = {1, 2, 3, 3, 4, 5}

print(S2)

print(S1)

# set() function :

S3 = set("python")
print(S3)

S4 = set([10,20,20,30,40,50])
print(S4)

S5 = set((10,20,30,40,50))
print(S5)

# While Creating a set object, you can store only Numbers, Strings, Tuple
# list and Dictionary are not allowed

# Tuples are allowed
Set1 = {(10,20), 30, 40, 50}
print(Set1)

# List are not allowed
# Set2 = {[10, 70], 30, 40, 50}
# print(Set2)

# Set Operations
# Union : |
P1 = {1, 2, 3, 4, 5}
P2 = {4, 5, 6, 7, 8}

print(P1 | P2)
print(P1.union(P2))
print(P2.union(P1))

# Intersection : &
print(P1&P2)
print(P1.intersection(P2))

# Difference of sets : - or difference()
print(P1-P2)
print(P1.difference(P2))

# Symmetric Difference : ^
print(P1 ^ P2)
print(P1.symmetric_difference(P2))

# Set - In Built() Methods:
# 1. add()
A1 = {"Java","Python","Ruby"}
A1.add("Perl")
print(A1)

# 2. update()
A2 = {"Scala", "Python", "JS"}
A2.update(["Python", "VB"])
print(A2)

# 3. Clear()
A1.clear()
print(A1)

# 4. Copy()
lang = {"Bangla", "English", "Hindi"}
lang2 = lang.copy()
print(lang2)

# 5. Discard Method
lang2.discard("Bangla")
lang2.discard("French")
print(lang2)

# 6. Remove
Student = {"Tom", "Jerry", "Panda"}
Student.remove("Panda")
print(Student)





