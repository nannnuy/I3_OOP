class Product:
    store_name = "ITC Online Store"
    product_count = 0

    def __init__(self, name, price, quantity):
        if not self.is_valid_price(price):
            raise ValueError(f"Your {price} should be positive")
        self.name = name
        self.price = price
        self.quantity = quantity

        Product.product_count += 1
        self.product_id = Product.product_count

    def display_product(self):
        print(f"Product {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")


    def total_value(self):
        return self.price * self.quantity

    @classmethod
    def get_product_count(cls):
        return cls.product_count


    @staticmethod
    def is_valid_price(price):
        return price > 0 

product1 = Product("Laptop", 800, 5)
product2 = Product("Mouse", 15, 20)
product3 = Product("Keyboard", 30, 10)

Products = [product1, product2, product3]

print(f"========== {Product.store_name} ==========")
total_inventory_value = 0

for product in Products:
    product.display_product()
    total_inventory_value += product.total_value()
    print()

print(f"Total Products: {Product.product_count}")
print(f"Total Inentory value: ${total_inventory_value}")