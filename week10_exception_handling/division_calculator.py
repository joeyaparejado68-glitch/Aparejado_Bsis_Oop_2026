try:
    first_value = float(input("Enter first number: "))
    second_value = float(input("Enter second number: "))

    quotient = first_value / second_value

    print("Result:", quotient)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid numeric input.")