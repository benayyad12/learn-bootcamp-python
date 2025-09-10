bill=float(input("What is the total bill?\n"))
people=int(input("number of person:\n"))
tip=int(input("tip: 10 or 12 or 15\n"))

tip_bill = bill + bill * tip/100
bill_person = tip_bill / people 
print(f"each person should pay: {round(bill_person,2)}")
