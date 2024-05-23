# While Loop

counter = 0;
while counter < 5:
    print("Hello World")
    counter = counter + 1

print("-----------------------")
# While Loop with Else

num = 0
while num < 3:
    print("While Loop Executes")
    num = num + 1
else:
    print("While loop exits")

print("-----------------------")
# For Loop

name = ["Java", "Python", "PHP", "C"]
for i in name:
    print(i)


print("-----------------------")
# For String Loop
String = "Python is Best"
for i in String:
    print(i)


print("--------------------------")
# For Loop with index and range
listArray = ["Naveen","Automation","Labs"]
for index in range(len(listArray)):
    print(listArray[index])

print("--------------------------")
# For Loop with else
CountryList = ["USA","India","UK"]
for index in range(len(CountryList)):
    print(CountryList[index])
else:
    print("CountryList is over")


print("--------------------------")
# Nested for loop
for i in range(1,5):
    for j in range(i):
        print(i, end='')
    print()


