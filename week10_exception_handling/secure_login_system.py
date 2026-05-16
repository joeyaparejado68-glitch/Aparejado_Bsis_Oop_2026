try:
    mja_user = input("Enter username: ")
    mja_pass = input("Enter password: ")

    if mja_user == "" or mja_pass == "":
        print("Username and password cannot be empty.")

    else:
        if mja_user == "marvin joey" and mja_pass == "123":
            print("Login Successful!")

        else:
            print("Invalid username or password.")

except Exception:
    print("Error: Incorrect input format.")