# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if num1 < num2:
            print(f"The smaller number is: {num1}")
        elif num2 < num1:
            print(f"The smaller number is: {num2}")
        else:
            print("Both numbers are equal.")
        break
    
    except ValueError: 
        print("Please enter a valid number.")
        continue