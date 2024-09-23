# welcome display
print("Welcome to the Simple Calculator!")
# Ask the user to input two numbers 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Step 2: Ask for the operation
operation = input("Choose the operation (+, -, *, /): ")
# Step 3: Use match-case to perform the calculation
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")    
    case "/":
        if num2 == 0:
            print("Error")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
            print("Invalid operation. Please choose +, -, *, or /.")