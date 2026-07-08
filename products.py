class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def add_quantity(self, quantity):
        self.quantity += quantity
        if self.quantity == 0:
            self.active = False
        else:
            self.active = True

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def is_active(self):
        return self.active

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if self.quantity >= quantity:
            self.add_quantity(-quantity)
            return self.price * quantity
        else:
            print(f"Not enough products in store, only {self.quantity} in stock.")
            return 0.0
