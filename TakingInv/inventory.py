# This is a program that makes what the bone heads at my job couldn't do, a basic inventory system

class Inventory:
    def __init__(self, department, category, style, price):
        self.department = department
        self.category = category
        self.style = style
        self.price = price

    def credit_card_price(self):
        return "10% TJX Credit Card Coupon Price: ${0:.3g}".format(self.price * (.9))

    def display_info(self):
        print("Dept: {} \nCatg: {}\nStyle: {}\nBase Price: ${}".format(self.department, self.category, self.style, self.price))
