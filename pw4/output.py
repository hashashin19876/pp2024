# Import necessary curses libraries
import curses

def list_courses(courses):
  # Use curses library to display courses in a formatted way
  for course in courses:
    print(course)

def list_students(students):
  # Use curses library to display students in a formatted way
  for student in students:
    print(student)

def show_marks(marks, course_id):
  # Use curses library to display marks for a course
  for mark in marks:
    if mark.course_id == course_id:
      print(f"Student ID: {mark.student_id}, Mark: {mark.mark}")

def calculate_gpa(student):
  # Use curses library to display GPA for a student
