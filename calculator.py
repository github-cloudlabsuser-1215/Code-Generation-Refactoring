# Create a basic calculator that can do the following operations:
# Add, Subtract, Multiply, Divide, Modulus, Exponentiation and Floor Division
# The calculator should be able to handle both integers and floats.
# The calculator should be able to handle both positive and negative numbers.
# The calculator should be able to handle division by zero.
# The calculator should be able to handle invalid inputs.
# The calculator should be able to handle invalid operations.
# The calculator should be able to handle invalid numbers.
# The calculator should be able to handle invalid number of arguments.
# The calculator should be able to handle invalid number of operations.
# The calculator should be able to handle invalid number of operands.
# The calculator should be able to handle invalid number of operators.
# The calculator should be able to handle invalid number of operands and operators.
# The calculator should be able to handle invalid number of operands and operations.
# The calculator should be able to handle invalid number of operators and operations.
# The calculator should be able to handle invalid number of operands, operators and operations.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero"

    def modulus(self, a, b):
        return a % b

    def exponentiate(self, a, b):
        return a ** b

    def floor_divide(self, a, b):
        try:
            return a // b
        except ZeroDivisionError:
            return "Error: Division by zero"

    def calculate(self, operation, a, b):
        operations = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'modulus': self.modulus,
            'exponentiate': self.exponentiate,
            'floor_divide': self.floor_divide
        }
        if operation not in operations:
            return "Error: Invalid operation"
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            return "Error: Invalid number"
        return operations[operation](a, b)

if __name__ == "__main__":
    calc = Calculator()
    while True:
        user_input = input("Enter operation and two numbers (e.g., add 1 2): ").split()
        if len(user_input) != 3:
            print("Error: Invalid input")
            continue
        operation, num1, num2 = user_input
        result = calc.calculate(operation, num1, num2)
        print(f"Result: {result}")
    