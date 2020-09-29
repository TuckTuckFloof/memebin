class Inventory:
    def __init__(self, department, category, style, price, desc):
        self.department = department
        self.category = category
        self.style = style
        self.price = price
        self.desc = desc

    def get_department(self):
        print(self.department)
    
    def get_category(self):
        print(self.category)

    def get_style(self):
        print(self.style)

    def get_price(self):
        print(self.price)

    def get_desc(self):
        print(self.desc)

    def set_department(self, department):
        self.department = department

    def set_category(self, category):
        self.category = category

    def set_style(self, style):
        self.style = style

    def set_price(self, price):
        self.price = price

    def set_desc(self, desc):
        self.desc = desc

    def credit_card_price(self):
        return "10% TJX Credit Card Coupon Price: ${0:.3g}".format(self.price * (.9))

    def display_info(self):
        print("Dept: {} \nCatg: {}\nStyle: {}\nBase Price: ${}\nDescription: {}\n".format(self.department, self.category, self.style, self.price, self.desc))
