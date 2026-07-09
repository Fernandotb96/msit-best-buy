import products
import store

# Initial setup of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def print_menu():
    print("""
    Welcome to Best Buy Shop!
    -----------------------------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
    """)


def print_products_stock(shop):
    print("----- Products in stock -----")
    shop_products = shop.get_all_products()
    for product in shop_products:
        print(f"{product.name}, Price: {product.price}$, Quantity: {product.quantity}")
    print("-" * 30)


def print_quantity(shop):
    print("----- Total stock amount -----")
    products_quantity = shop.get_total_quantity()
    print(f"Total Quantity: {products_quantity} products")


def make_order(shop):
    pass
