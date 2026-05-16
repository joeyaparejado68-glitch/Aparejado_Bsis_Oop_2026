while True:
    try:
        entered_num = int(input("Enter a number: "))
        break

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("Valid number entered:", entered_num)

