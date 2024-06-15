import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier


def main():
    sandwich_machine = SandwichMaker(resources)
    inserted_coins = 0
    cost_of_sammy = 0
    change = 0

    print("Welcome to my sandwich maker! ")
    print("Order a small, medium, or large sandwich, report number of ingredients, or turn the machine off!")
    sandwich_type = input("Valid options are 'small', 'medium', 'large', 'off', or 'report': ")
    while sandwich_type != "off":
        if sandwich_type == "report":
            print("Bread: ", resources["bread"])
            print("Ham: ", resources["ham"])
            print("Cheese: ", resources["cheese"])
        elif sandwich_type == "small" or sandwich_type == "medium" or sandwich_type == "large":
            if sandwich_machine.check_resources(recipes[sandwich_type]["ingredients"]):
                inserted_coins = cashier_instance.process_coins(sandwich_maker_instance)
                cost_of_sammy = recipes[sandwich_type]["cost"]
                if cashier_instance.transaction_result(sandwich_maker_instance, inserted_coins, cost_of_sammy):
                    sandwich_machine.make_sandwich(sandwich_type, recipes[sandwich_type]["ingredients"])
                    print("Your", sandwich_type, "sandwich is ready")
        else:
            print("Sorry, that's not a valid option")
        sandwich_type = input("What would you like? (small, medium, large, off, report): ")

        if sandwich_type == "off":
            print("Bye bye!")


if __name__ == "__main__":
    main()
