# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        start = min(num1, num2)
        stop = max(num1, num2)

        if start == stop:
            print("There are no numbers between the same number.")

        else:
            for i in range(start + 1, stop):
                print(i)
            
        break
    except ValueError:
        print("Please enter a valid number.")
