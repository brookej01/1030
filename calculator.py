# Simple Calculator module

# Function to add
def add_numbers(first_number, second_number):
    return first_number + second_number

# Function to subtract
def subtract_numbers(first_number, second_number):
    return first_number - second_number

# Function to multiply
def multiply_numbers(first_number, second_number):
    return first_number * second_number

# Function to divide
def divide_numbers(first_number, second_number):
    if second_number == 0:
        print("Cannot divide by zero")
        return None
    return first_number / second_number

print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

if operation == "add":
    result = add_numbers(first_number, second_number)
    print(f"Result: {result}")
elif operation == "subtract":
    result = subtract_numbers(first_number, second_number)
    print(f"Result: {result}")
elif operation == "multiply":
    result = multiply_numbers(first_number, second_number)
    print(f"Result: {result}")
elif operation == "divide":
    result = divide_numbers(first_number, second_number)
    if result is not None:
        print(f"Result: {result}")
    
else:
    print("Sorry, I do not understand your request.")