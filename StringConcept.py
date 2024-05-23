S1 = "hello world"
S2 = "test Selenium"

print(S1+" "+S2)

print("Hello \n World")
print("Hello \t World")

print("hello" in S1)
print("hello" not in S1)

# Formatting Operator
print("My name is %s and My age is %d" %("Mahbub",29))

# Special Paragraph
S3 = '''Java is popular language but 
nowadays python is more convenient and
that why I love Python'''

print(S3)

print('Hello I\'m Mahbub')
print("\"Java\" is good but \"python\" is best")

str1 = "this is my python code & python is best"
print(str1)
print(str1.capitalize())
print(str1.count("python"))
print(str1.find("code"))
print(len(str1))

str2 = "  Hello  "
print(str2.lstrip())
print(str2.rstrip())
print(max(str1))

str3 = "Hello Python Test"
print(str3.replace("Hello", "Bye"))

str4 = "Java hello python hello javascript"
str5 = str4.split("hello")
print(str5)
print(str4.upper())

