# 2.student.mark.py

students = []
courses = []
marks = []

def input_number_of_students():
    num = int(input("Enter number of students: "))
    return num

def input_student_info():
    name = input("Enter student name: ")
    id = input("Enter student id: ")
    dob = input("Enter student DoB: ")
    major = input("Enter student major:")

    students.append({"id": id, "name": name, "dob": dob, "major": major})

def input_number_of_courses():
    num = int(input("Enter number of courses: "))
    return num
def input_name_of_courses():
    name = int(input("Enter name of courses:"))
    return name
      
def input_course_info():
    id = input("Enter course id: ")
    name = input("Enter course name: ")
    courses.append({"id": id, "name": name})

def input_marks():
    course_id = input("Select a course by id: ")
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']}: "))
        marks.append({"student_id": student["id"], "course_id": course_id, "mark": mark})

def list_courses():
    for course in courses:
        print(course)

def list_students():
    for student in students:
        print(student)

def show_marks():
    course_id = input("Select a course by id: ")
    for mark in marks:
        if mark["course_id"] == course_id:
            print(f"Student ID: {mark['student_id']}, Mark: {mark['mark']}")

def main():
    num_students = input_number_of_students()
    for _ in range(num_students):
        input_student_info()

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        input_course_info()

    input_marks()

    list_courses()
    list_students()
    show_marks()

if __name__ == "__main__":
    main()
