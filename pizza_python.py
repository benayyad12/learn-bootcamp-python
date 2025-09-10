size = input("Enter size of pizza: S,M,L:\n")
pepperoni = input("Do you want to add pepperoni: Y or N:\n")
extra_cheese = input("Do you want extra cheese: Y or N:\n")
bill=0

if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25
else:
    print("Error")

if pepperoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3
if extra_cheese == "Y":
    bill+=1

print(f"Your Total bill is: {bill}$")