print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?:\n"))
    if age >= 18:
        bill=12
        print("you pay 12$")
    elif age <= 12:
        bill=5
        print("you pay 5$")
    else:
        bill=7
        print("you pay 7$")

    want_photo = input("Do you want a photo take? Yes or No")
    if want_photo.lower() == "yes":
        bill+=3
    print(f"Final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
