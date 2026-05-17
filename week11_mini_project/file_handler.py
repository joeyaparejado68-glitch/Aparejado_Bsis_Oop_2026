def save_student(mja_student):

    with open("students.txt", "a") as mja_file:

        mja_file.write(
            mja_student.mja_id + "," +
            mja_student.mja_name + "," +
            mja_student.mja_course + "\n"
        )


def view_students():

    try:

        with open("students.txt", "r") as mja_file:

            for mja_line in mja_file:

                mja_id, mja_name, mja_course = mja_line.strip().split(",")

                print(mja_id, mja_name, mja_course)

    except FileNotFoundError:

        print("No records found.")