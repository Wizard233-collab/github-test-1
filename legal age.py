#if statement

age = ("The legal age for a person to vote is (18 years and older)")
age = int(input("Enter the age:"))

if age >=18:
    print("This person is eligible to vote!")
elif age ==0:
   print("This person has not yet been born!")
elif age >=105:
  print("This person is not eligible to vote!")
elif age <=18:
  print("This person has not reached the legal voting age!")
