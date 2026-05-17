class Student:
    def __init__(self, mja_id, mja_name, mja_course):
        self.mja_id = mja_id
        self.mja_name = mja_name
        self.mja_course = mja_course

    def display_info(self):
        print(self.mja_id, self.mja_name, self.mja_course)


student1 = Student("2026-001", "MJA", "BSIS")
student1.display_info()