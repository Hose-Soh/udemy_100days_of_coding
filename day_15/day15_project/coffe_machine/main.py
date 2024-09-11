from resource import resources, show_report, MENU
import serve_coffee

def main():
    while True:
        # add a new key money in resources if it's not already existed and assign zero as value
        if "money" not in resources.keys():
            resources["money"] = 0

        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input=='report':
            show_report(resources)
        elif user_input=='off':
            return
        elif user_input=='latte':
            serve_coffee.serve_latte(resources, MENU)
        elif user_input=='espresso':
            serve_coffee.serve_espresso(resources, MENU)
        elif user_input=='cappuccino':
            serve_coffee.serve_cappuccino(resources, MENU)
        else:
            continue


if __name__ == "__main__":
    main()