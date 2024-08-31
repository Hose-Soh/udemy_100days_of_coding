print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
total_bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Children Ticket Price $5.")
        total_bill = 5
    elif age <= 18:
        print("Youth Ticket Price $7.")
        total_bill = 7
    else:
        print("Adult Ticket Price $12.")
        total_bill = 12

    photo = int(input("Do you want photo? Type 1 for YES, 0 for NO: "))
    if photo ==1:
        total_bill+=3

    print(f"You have to pay total ${total_bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
