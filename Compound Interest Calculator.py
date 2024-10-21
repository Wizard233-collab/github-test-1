principal = 0
rate = 0
time = 0

while True:
  principal = float (input("Enter the principal amount:"))
  if principal < 0:
    print("principal cannot be less than zero")
  else:
    break


while True:
  rate = float(input("Enter the interst rate:"))
  if rate < 0:
    print("The interest rate cannot be less than zero")
  else:
    break


while True:
  time = int(input("Enter the number of years:"))
  if time < 0:
    print("The number of years cannot be less than zero")
  else:
    break


    
    
total = principal * pow(1 + rate / 100, time)
print(f"Balance after {time} year/s: ${total:.2f}")