print("topic covered are: varaible, operators (addition/ sub etc), conditions (if, elif, else), loops (for, while), list, print f")


num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))

sum = num1 + num2

print("sum is : ", sum)

print(f"multiplicaton of {num1} and {num2} is {num1*num2}")

if (sum % 2 == 0):
    print("even")
else: 
    print("odd")
    

if 0 <= num1 <= 99 and num1 % 2 == 0:
    print("num1 is between 0 to 99 and even")
elif 0 <= num1 <= 99 and num1 % 2 != 0:
    print("num1 is between 0 to 99 and odd")
elif 0 <= num1 <= 99 or num1 % 2 == 0:
    print("num1 is between 0 to 99 or even")
    
    
i = 0

while i <= 5:
    print(f"i : {i}")
    i += 1
    
for j in range(0, 6):
    print(f"j : {j}")
    

vehicles = ["bus", "car", "truck", "bike", "rickshaw"]

for vehicle in vehicles:
    print(vehicle)
    

mixed_list = ["house", True, 12, "car", "tree", 12.3]

for element in mixed_list:
    print(f"element: {element}, type: {type(element)}")




num3 = int(input("enter num3: "))
num4 = int(input("enter num4: "))


if num3 > num4:
    sub = num3 - num4
    print(f"subtraction is: {sub}")

for x in range (1, num3 + 1):
    print(f"x: {x}")


list = [12, 93, 88, 23, 0]

for element in list:
    print(f"element: {element}")


name = "john"
age = 23

print(f"type of name is: {type(name)}")
print(f"type of age is: {type(age)}")