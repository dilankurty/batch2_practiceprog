# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
        
if num2 == 0:
    print("Cannot divide by zero.")
else:
    print(f"Remainder: {num1%num2}")