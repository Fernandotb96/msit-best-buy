class Store:

    def __init__(self, products_list):
        if products_list is None:
            self.products_list = []
        else:
            self.products_list = products_list

    def add_product(self, product):
        self.products_list.append(product)

    def remove_product(self, product):
        if product in self.products_list:
            self.products_list.remove(product)
        else:
            print(f"Product {product.name} not in store.")

    def get_total_quantity(self):
        total = 0
        for product in self.products_list:
            total += product.quantity
        return total

    def get_all_products(self):
        active_products = []
        for product in self.products_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_cart):
        total_price = 0
        for product, quantity in shopping_cart:
            if product in self.products_list:
                total_price += product.buy(quantity)
            else:
                print(f"Error, product {product.name} not in store.")
        return total_price
