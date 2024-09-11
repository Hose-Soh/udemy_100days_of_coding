def update_resource(drink_details, res, money_inserted, drink_name):
    res["water"] = res["water"] - drink_details[drink_name]["ingredients"]["water"]
    res["coffee"] = res["coffee"] - drink_details[drink_name]["ingredients"]["coffee"]
    res["money"] = res["money"] + drink_details[drink_name]["cost"]
    if drink_name != "espresso":
        res["milk"] = res["milk"] - drink_details[drink_name]["ingredients"]["milk"]

    if money_inserted > drink_details[drink_name]["cost"]:
        money_change = money_inserted - drink_details[drink_name]["cost"]
        print(f"Here is ${round(money_change, 2)} dollars in change")


def payment_process(res, drink_details, name):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    total_inserted_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total_inserted_money >= drink_details[name]["cost"]:
        update_resource(drink_details, res, total_inserted_money, name)
        print(f"Here is your {name}. Enjoy!")
    else:
        print(f"Sorry that's not enough money. Money refunded.")