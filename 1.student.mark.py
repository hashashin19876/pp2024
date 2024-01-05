# 1.student.mark.py

students = []
courses = []
marks = []

def input_number_of_students():
    num = int(input("Enter number of students: "))
    return num

def input_student_information(num):
    for i in range(num):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        students.append((id, name, dob))

def input_number_of_courses():
    num = int(input("Enter number of courses: "))
    return num

def input_course_information(num):
    for i in range(num):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append((id, name))

def input_marks_for_course():
    course_id = input("Enter course id to input marks: ")
    for student in students:
        mark = input(f"Enter mark for student {student[1]}: ")
        marks.append((student[0], course_id, mark))

def list_courses():
    print("Courses:")
    for course in courses:
        print(course)

def list_students():
    print("Students:")
    for student in students:
        print(student)

def show_marks_for_course():
    course_id = input("Enter course id to show marks: ")
    for mark in marks:
        if mark[1] == course_id:
            print(f"Student {mark[0]} got {mark[2]}")

num_students = input_number_of_students()
input_student_information(num_students)
num_courses = input_number_of_courses()
input_course_information(num_courses)
input_marks_for_course()
list_courses()
list_students()
show_marks_for_course()
