# Weight Converter Program


Input = input("Converting from:")
output = input("Converting to:")
Value = int(input("Enter the value:"))

if Input == "kilograms" and output == "grams":
    Results = Value * 1000
    print(f"The answer is {Results} grams!")

elif Input == "kilograms" and output == "pounds":
    Results = Value * 2.205
    print(f"The answer is {Results} pounds!")

elif Input == "kilograms" and output == "ounces":
    Results = Value * 35.274
    print(f"The answer is {Results} ounces!")

elif Input == "grams" and output == "kilograms":
    Results = Value / 1000
    print(f"The answer is {Results} kilograms!")

elif Input == "grams" and output == "pounds":
    Results = Value / 453.6
    print(f"The answer is {Results} pounds!")

elif Input == "grams" and output == "ounces":
    Results = Value / 28.35
    print(f"The answer is {Results} ounces!")

elif Input == "pounds" and output == "kilograms":
    Results = Value / 2.205
    print(f"The answer is {Results} kilograms!")

elif Input == "pounds" and output == "grams":
    Results = Value * 453.6
    print(f"The answer is {Results} grams!")

elif Input == "pounds" and output == "ounces":
    Results = Value * 16
    print(f"The answer is {Results} ounces!")

elif Input == "ounces" and output == "kilograms":
    Results = Value / 35.274
    print(f"The answer is {Results} kilograms!")

elif Input == "ounces" and output == "grams":
    Results = Value * 28.35
    print(f"The answer is {Results} grams!")

elif Input == "ounces" and output == "pounds":
    Results = Value / 16
    print(f"The answer is {Results} pounds!")

else:
    print("What you have entered is invalid")






    



    




