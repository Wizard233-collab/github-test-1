# Program that checks if a user is eligible for a certain membership based on their age and current membership status

user = int(input("Enter the age:"))
member = input("Are you a member of this country(Y for Yes / N for No:)")

if user == 18 or user > 18 and member == "N":
    print("This user is eligible for membership!")

elif user < 18 and member == "Y":
    print("This user is eligible for membership!")

else:
    print("This user is not eligible for membership!")
