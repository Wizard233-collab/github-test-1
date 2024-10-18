#python calculator

operator = input("Enter the operator (+ - * /):")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if operator == "+":
    result= num1 + num2
    print(result)

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":
    result = num1 / num2
    print(result)

else:
    print(f"The {operator} is not valid")