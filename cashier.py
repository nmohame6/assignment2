class Cashier:
    def __init__(self):
        pass


    def process_coins(coins):
        """Returns the total calculated from coins inserted."""
        dollars = input("How many dollars?: ")
        half_dollars = input("How many half dollars?: ")
        quarters = input("How many quarters?: ")
        dimes = input("How many dimes?: ")
        total = float(dollars) + float(half_dollars) * 0.5 + float(quarters) * 0.25 + float(dimes) * 0.1
        return total


    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = float(coins - cost)
            print("We're preparing your sandwich! Your change is: $", change)
            return True
        else:
            print("Sorry, that's not enough money, come back and try your order With more money or a smaller sandwich")
            return False
