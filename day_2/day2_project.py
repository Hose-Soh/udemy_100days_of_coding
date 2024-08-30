print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_per_person = bill/people
tip_per_person = bill_per_person*tip/100
bill_split = round(bill_per_person+tip_per_person, 2)
print(f"Each person should pay: ${bill_split}")