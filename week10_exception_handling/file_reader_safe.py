try:
    with open("data.txt", "r") as my_file:
        file_content = my_file.read()

    print(file_content)

except FileNotFoundError:
    print("Error: File does not exist.")