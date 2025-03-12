def  greeting():
    print("Hello!")

def greeting_w_name(name):
    print(f"Hello {name}!")

def add(a, b):
    print(a + b)

#greeting()
# greeting_w_name("Micah")
# greeting_w_name("Simone")
# greeting_w_name("Isiah")
add(5, 10)
add(3, 4)
add(16, 7)

def subtract(a, b):
    print(a - b)
subtract(60, 5)    
subtract(10, 7)

def divide(a, b):
    print(a / b)
divide(15, 5)
divide(10, 2)

def multiply(a, b):
    print(a * b)
multiply(10 * 10)
multiply(5 * 3)

operation = input("Which operation do you want to use (+, -, *, /): ")
a = input("Enter your first number: ")
b = input("Enter your second number: ")

if operation == "+":
    add(a, b)
elif operation == "-":
    subtract(a, b)
elif operation == "/":
    multiply(a, b)
elif operation == "*":
    divide(a, b)
