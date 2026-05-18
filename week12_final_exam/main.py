from product import Product
from inventory_manager import add_product, view_products


def search_mja():
    mja_id = input("Enter Product ID: ")

    try:
        with open("products.txt", "r") as mja_file:

            for mja_line in mja_file:
                mja_data = mja_line.strip().split(",")

                if mja_data[0] == mja_id:
                    print("Product Found:", mja_line)
                    return

            print("Product not found")

    except FileNotFoundError:
        print("Inventory file not found")


while True:

    print("\nINVENTORY MANAGEMENT SYSTEM")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Exit")

    mja_choice = input("Enter choice: ")

    if mja_choice == "1":

        try:
            mja_product_id = input("Enter Product ID: ")
            mja_name = input("Enter Product Name: ")
            mja_price = float(input("Enter Price: "))
            mja_quantity = int(input("Enter Quantity: "))

            mja_product = Product(
                mja_product_id,
                mja_name,
                mja_price,
                mja_quantity
            )

            add_product(mja_product)

            print("Product added successfully")

        except ValueError:
            print("Invalid input")

    elif mja_choice == "2":
        view_products()

    elif mja_choice == "3":
        search_mja()

    elif mja_choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid option")