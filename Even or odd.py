#if statement

number = ("The number is either an even or odd number!")
number = int(input("Enter the number:"))

if number % 2==0:
    print(f"This {number} is an even number!")
else:
    print(f"This {number} is an odd number!")
    