
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        if self.machine_resources["bread"] >= ingredients["bread"]:
            if self.machine_resources["ham"] >= ingredients["ham"]:
                if self.machine_resources["cheese"] >= ingredients["cheese"]:
                    return True
        else:
            if self.machine_resources["bread"] < ingredients["bread"]:
                print("Sorry, we don't have enough bread")
            if self.machine_resources["ham"] < ingredients["ham"]:
                print("Sorry, we don't have enough ham")
            if self.machine_resources["cheese"] < ingredients["cheese"]:
                print("Sorry, we don't have enough cheese")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
                   Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
