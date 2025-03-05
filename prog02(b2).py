# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if num1 != num2:
            print("Not Equal")
        else:
            print("Both numbers are equal.")
        break
    
    except ValueError: 
        print("Please enter a valid number.")
        continue