import math

# Function to perform the calculation
def perform_calculation(num1, num2, operation):
    if operation == 1:  # Addition
        result = num1 + num2
        return f"Addition: {num1} + {num2} = {result}"
    elif operation == 2:  # Subtraction
        result = num1 - num2
        return f"Subtraction: {num1} - {num2} = {result}"
    elif operation == 3:  # Multiplication
        result = num1 * num2
        return f"Multiplication: {num1} * {num2} = {result}"
    elif operation == 4:  # Division
        if num2 == 0:
            return "Error! Division by zero is not allowed."
        result = num1 / num2
        return f"Division: {num1} / {num2} = {result}"
    elif operation == 5:  # Square Root
        if num1 < 0:
            return "Error! Cannot compute square root of a negative number."
        result = math.sqrt(num1)
        return f"Square Root: √{num1} = {result} (and {result}^2 = {num1})"
    elif operation == 6:  # Exponentiation
        result = math.pow(num1, num2)
        return f"Exponentiation: {num1}^{num2} = {result}"
    elif operation == 7:  # Modulus
        result = num1 % num2
        return f"Modulus: {num1} % {num2} = {result}"
    elif operation == 8:  # Sine (in radians)
        result = math.sin(math.radians(num1))  # Convert to radians
        return f"Sine: sin({num1}°) = {result}"
    elif operation == 9:  # Cosine (in radians)
        result = math.cos(math.radians(num1))  # Convert to radians
        return f"Cosine: cos({num1}°) = {result}"
    elif operation == 10:  # Tangent (in radians)
        result = math.tan(math.radians(num1))  # Convert to radians
        return f"Tangent: tan({num1}°) = {result}"
    else:
        return "Invalid operation. Please choose a valid option."

# Main function to run the calculator
def calculator():
    print("Welcome to the Enhanced Scientific Calculator!")
    print("Select an operation by entering the number:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Modulus")
    print("8. Sine (degrees)")
    print("9. Cosine (degrees)")
    print("10. Tangent (degrees)\n")

    while True:
        # Taking user input for operation selection
        try:
            operation = int(input("Select the operation (1-10): "))
        except ValueError:
            print("Invalid input! Please select a number between 1 and 10.\n")
            continue

        # Ask for the appropriate number of inputs based on the operation
        if operation in [1, 2, 3, 4, 6, 7]:  # Operations that require 2 inputs
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter valid numbers.\n")
                continue
        elif operation in [5, 8, 9, 10]:  # Operations that require 1 input
            try:
                num1 = float(input("Enter the number: "))
                num2 = None  # Set num2 to None for single input operations
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")
                continue
        else:
            print("Invalid operation. Please choose a valid option.\n")
            continue

        # Perform the calculation and display the result
        result = perform_calculation(num1, num2, operation)
        print(f"Result: {result}\n")

        # Ask if the user wants to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != "yes":
            print("Thank you for using the calculator! Goodbye.")
            break

# Run the calculator
if __name__ == "__main__":
    calculator()
