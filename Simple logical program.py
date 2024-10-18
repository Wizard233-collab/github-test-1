# Logical Operators = ("It is used to check whether two or more conditional statements are true using (and,not,or)")

temp = int(input("What is the temperature outside? :"))

if not (temp >=0 and  temp <=30):
    print("the temperature is bad today!")
    print("stay inside!")

elif not  (temp <=0 or temp >=30):
    print("the temperature is very good today!")
    print("go outside!")