#print("Hello World")

# Simple Python Application for Addition

def add_numbers(num1, num2):
    return num1 + num2

try:
    # Get user input
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Add the two numbers
    result = add_numbers(number1, number2)

    # Display the result
    print(f"The sum of {number1} and {number2} is {result}.")

except ValueError:
    print("Please enter valid numbers.")

