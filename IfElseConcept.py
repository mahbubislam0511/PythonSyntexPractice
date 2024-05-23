
x = int(input("Please Enter the value of X : "))
print(x)

if x<0:
    print("X is negative number")
elif x>0:
    print("X is positive number")
elif x==0:
    print("X is equal to zero")
else:
    print("X is not defined")

# Write a program to find out the highest number

a = 200
b = 800
c = 500

if a > b and a > c:
    print("a is the highest number")
elif b > c:
    print("b is the highest number")
else:
    print("c is the highest number")

# Take an input and check some mathematics
total = int(input("Enter the total value : "))

if total<100:
    total = total+20
elif 100 <= total <= 500:
    total = total+50
else:
    total = total+100
print("Total is : "+str(total)) # Str method
print(f'{"Total is : "}{total}') # If String method







