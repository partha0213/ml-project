# Stage 1: Basic Calculator

def basic_calculator():
    print("Welcome to Basic Calculator")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2
            print(f"Result = {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"Result = {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"Result = {result}")
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result = {result}")
        else:
            print("Invalid operator.")
            
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    basic_calculator()
