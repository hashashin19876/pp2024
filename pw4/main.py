from course_marks_system.domains import CourseMarkSystem
from input import input_student, input_course, input_marks
from output import list_courses, list_students, show_marks, calculate_gpa  # Assuming output.py uses curses

def main():
  system = CourseMarkSystem()
  num_students = int(input("Enter number of students: "))
  for _ in range(num_students):
    student = input_student()
    system.students.append(student)

  num_courses = int(input("Enter number of courses: "))
  for _ in range(num_courses):
    course = input_course()
    system.courses.append(course)

  input_marks(system)

  list_courses(system.courses)
  list_students(system.students)
  course_id = input("Select a course by id to see marks: ")
  show_marks(system.marks, course_id)
  student_id = input("Select a student by id to calculate GPA: ")
  student = next(student for student in system.students if student.id == student_id)
  calculate_gpa(student)  # Modify this line based on your output implementation

if __name__ == "__main__":
  main()
