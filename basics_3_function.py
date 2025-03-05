# Basic function in python
def print_message():
    print("hello world")

print_message()

# function with parameters
def add(x, y):
    print(f"x: {x}, y: {y}")
    return x + y

print(f"sum of 2 and 3 is {add(2, 3)}")
print(f"sum of 3 and 10 is {add(y=10, x=3)}")

# function with default parameters
def greet(name="Guest"):
    print(f"Hello {name}!")

greet("John")
greet()

# another function with default parameters
def greet(name="Guest", pre_message="Dear", message="Good Morning"):
    print(f"{message} {pre_message} {name}!")

greet()
greet("John", "Dear", "Good Evening")
greet("John")
greet(message="Good Evening", pre_message="Honorable")


# function with variable number of arguments
def sum_all(*args):
    return sum(args)

result = sum_all(3, 2, 8, 2, 10)

print(f"sum of all numbers is {result}")

# function with variable number of keyword arguments
def print_all(**kwargs):
    print(kwargs)   

print_all(name="John", age=25, country="USA")

# another function with variable number of keyword arguments
def print_all_with_loop(**kwargs): 
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_all_with_loop(name="doe", age=51, country="UK")

# another function with variable number of keyword arguments
def print_Keys(**kwargs):
	for key in kwargs.keys():
		print(f"{key}")

print_Keys(name="doe", age=51, country="UK")

# practice day 2
def devide(i, j):
     return i / j

print(f"division of 4 / 2 is {devide(j = 4, i = 2)}")


def print_bill(total_bill = 0):
    print(f"total bill is {total_bill}")


print_bill(100)
print_bill()


def print_car_info(**kwargs):
     for key, value in kwargs.items():
         print(f"{key} : {value}")

print_car_info(brand = "toyota", model = "corolla", year = 2019)



