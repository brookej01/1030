# Importing previously made calculator module
import calculator

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter the operation (add/subtract/multiply/divide): ")

if operation in ("add", "subtract", "multiply", "divide"):
    if operation == "add":
                result = calculator.add_numbers(first_number, second_number)
    elif operation == "subtract":
                result = calculator.subtract_numbers(first_number, second_number)
    elif operation == "multiply":
                result = calculator.multiply_numbers(first_number, second_number)
    elif operation == "divide":
                result = calculator.divide_numbers(first_number, second_number)

    print(f"Result: {result}")
else:
            print("Invalid operation. Please enter 'add', 'subtract', 'multiply', or 'divide'.")