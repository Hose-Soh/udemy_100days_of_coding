import payment


def check_ingredients(res, menu, drink_name):
    all_okay = True
    not_sufficient_string = []

    if res["water"] >=menu[drink_name]["ingredients"]["water"]:
        all_okay*=True
    else:
        not_sufficient_string.append("water")
        all_okay *= False
    if res["coffee"] >= menu[drink_name]["ingredients"]["coffee"]:
        all_okay *= True
    else:
        not_sufficient_string.append("coffee")
        all_okay *= False

    if drink_name != 'espresso':
        if res["milk"] >= menu[drink_name]["ingredients"]["milk"]:
            all_okay *= True
        else:
            not_sufficient_string.append("milk")
            all_okay *= False

    return all_okay, not_sufficient_string

def serve_latte(res, menu, name="latte"):
    green_signal, red_signal = check_ingredients(res, menu, name)
    if green_signal:
        payment.payment_process(res, menu, name)

    else:
        red_signal_string = ", ".join(red_signal)
        print(f"Sorry there is not enough {red_signal_string}.")


def serve_espresso(res, menu, name="espresso"):
    green_signal, red_signal = check_ingredients(res, menu, name)
    if green_signal:
        payment.payment_process(res, menu, name)

    else:
        red_signal_string = ", ".join(red_signal)
        print(f"Sorry there is not enough {red_signal_string}.")


def serve_cappuccino(res, menu, name="cappuccino"):
    green_signal, red_signal = check_ingredients(res, menu, name)
    if green_signal:
        payment.payment_process(res, menu, name)

    else:
        red_signal_string = ", ".join(red_signal)
        print(f"Sorry there is not enough {red_signal_string}.")