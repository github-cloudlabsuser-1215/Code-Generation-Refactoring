# Create a basic calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by zero error"

# Calculator operations
def calculate(operation, x, y):
    if operation == "add":
        return add(x, y)
    elif operation == "subtract":
        return subtract(x, y)
    elif operation == "multiply":
        return multiply(x, y)
    elif operation == "divide":
        return divide(x, y)
    else:
        return "Invalid operation"



if __name__ == "__main__":
    # Run the calculator
    print("Welcome to the Calculator!")
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide) or 'quit' to exit: ")
        if operation == "quit":
            break
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        result = calculate(operation, x, y)
        print("Result:", result)

