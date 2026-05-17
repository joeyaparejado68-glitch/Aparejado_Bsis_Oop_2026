from student import Student
from file_handler import save_student, view_students


def add_mja_student():

    mja_id = input("Enter Student ID: ")
    mja_name = input("Enter Name: ")
    mja_course = input("Enter Course: ")

    mja_student = Student(mja_id, mja_name, mja_course)

    save_student(mja_student)

    print("Student added successfully")


def search_mja_student():

    mja_search_id = input("Enter Student ID to search: ")

    try:

        with open("students.txt", "r") as mja_file:

            for mja_line in mja_file:

                mja_id, mja_name, mja_course = mja_line.strip().split(",")

                if mja_id == mja_search_id:

                    print("Student Found:")
                    print(mja_id, mja_name, mja_course)

                    return

            print("Student not found")

    except FileNotFoundError:

        print("No records available")


while True:

    print("\nSTUDENT INFORMATION SYSTEM")
    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Exit")

    mja_choice = input("Enter choice: ")

    if mja_choice == "1":

        add_mja_student()

    elif mja_choice == "2":

        view_students()

    elif mja_choice == "3":

        search_mja_student()

    elif mja_choice == "4":

        break

    else:

        print("Invalid choice")