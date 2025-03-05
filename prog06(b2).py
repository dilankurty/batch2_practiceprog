# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

nums = []

for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            nums.append(num)
            break
        
        except ValueError: 
            print("Please enter a valid number.")
            continue

difference = nums[0] - sum(nums[1:])
print(difference)