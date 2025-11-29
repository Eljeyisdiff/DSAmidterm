import math

operator = input("Enter the operator (+, -, *, /, **, sqrt): ").lower()

def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Not a number. Please try again.")

def add():
    x = get_number("Enter the first number: ")
    y = get_number("Enter the second number: ")
    return x + y

def subtract():
    x = get_number("Enter the first number: ")
    y = get_number("Enter the second number: ")
    return x - y

def multiply():
    x = get_number("Enter the first number: ")
    y = get_number("Enter the second number: ")
    return x * y

def divide():
    x = get_number("Enter the first number: ")
    y = get_number("Enter the second number: ")
    if y == 0:
        print("Error: Cannot divide by zero!")
        return None
    return x / y

def power():
    x = get_number("Enter the number to square: ")
    return x ** 2

def square_root():
    x = get_number("Enter the number to square root: ")
    if x < 0:
        print("Error: Cannot take square root of negative number!")
        return None
    return math.sqrt(x)

match operator:
    case "+":
        print("The sum is", add())
    case "-":
        print("The difference is", subtract())
    case "*":
        print("The product is", multiply())
    case "/":
        result = divide()
        if result is not None:
            print("The quotient is", result)
    case "**":
        print("The square is", power())
    case "sqrt":
        result = square_root()
        if result is not None:
            print("The square root is", result)
    case _:    
        print("Invalid operator!")




