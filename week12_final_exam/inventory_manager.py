from product import Product


def add_product(product: Product, file_path: str = "products.txt"):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(product.to_line())


def view_products(file_path: str = "products.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]

        if not lines:
            print("No products in inventory")
            return

        print("Products in inventory:")
        for line in lines:
            fields = line.split(",")
            if len(fields) == 4:
                product_id, name, price, quantity = fields
                print(f"ID: {product_id} | Name: {name} | Price: {price} | Quantity: {quantity}")
            else:
                print("Invalid product record:", line)

    except FileNotFoundError:
        print("Inventory file not found")
