# Create a basic calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero."

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
        return "Error: Invalid operation."


def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    print("Welcome to the Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide) or 'quit' to exit: ").strip().lower()
        if operation == "quit":
            print("Thank you for using the calculator. Goodbye!")
            break
        if operation not in ("add", "subtract", "multiply", "divide"):
            print("Invalid operation. Please try again.")
            continue
        x = get_number("Enter first number: ")
        y = get_number("Enter second number: ")
        result = calculate(operation, x, y)
        print("Result:", result)

