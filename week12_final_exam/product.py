class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_line(self):
        return f"{self.product_id},{self.name},{self.price},{self.quantity}\n"

    def __str__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Price: {self.price} | Quantity: {self.quantity}"
