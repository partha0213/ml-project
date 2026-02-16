# Stage 2: Extended Calculator

def extended_calculator():
    print("Welcome to Extended Calculator")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        result = None

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
        else:
            print("Invalid operator.")

        if result is not None:
            print(f"Result = {result}")
            
            # Stage 2 Addition: Result Check
            if result > 0:
                print("Positive")
            elif result < 0:
                print("Negative")
            else:
                print("Zero")
            
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    extended_calculator()
