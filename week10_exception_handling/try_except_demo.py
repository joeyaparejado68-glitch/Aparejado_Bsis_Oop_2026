try:
    user_num = int(input("Enter any number: "))

    answer = 100 / user_num

    print("The result is:", answer)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Please enter a valid number.")