class Student:
  def __init__(self, id, name, dob):
    self.id = id
    self.name = name
    self.dob = dob

  def __str__(self):
    return f"Student ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

class Course:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def __str__(self):
    return f"Course ID: {self.id}, Name: {self.name}"

class Mark:
  def __init__(self, student_id, course_id, mark):
    self.student_id = student_id
    self.course_id = course_id
    self.mark = mark

  def __str__(self):
    return f"Student ID: {self.student_id}, Course ID: {self.course_id}, Mark: {self.mark}"

class CourseMarkSystem:
  def __init__(self):
    self.students = []
    self.courses = []
    self.marks = []

  def input_student(self):
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    dob = input("Enter student DoB: ")
    self.students.append(Student(id, name, dob))

  def input_course(self):
    id = input("Enter course id: ")
    name = input("Enter course name: ")
    self.courses.append(Course(id, name))

  def input_marks(self):
    course_id = input("Select a course by id: ")
    for student in self.students:
      mark = float(input(f"Enter mark for student {student.name}: "))
      self.marks.append(Mark(student.id, course_id, mark))

  def list_courses(self):
    for course in self.courses:
      print(course)

  def list_students(self):
    for student in self.students:
      print(student)

  def show_marks(self):
    course_id = input("Select a course by id: ")
    for mark in self.marks:
      if mark.course_id == course_id:
        print(f"Student ID: {mark.student_id}, Mark: {mark.mark}")

def main():
  system = CourseMarkSystem()
  num_students = int(input("Enter number of students: "))
  for _ in range(num_students):
    system.input_student()

  num_courses = int(input("Enter number of courses: "))
  for _ in range(num_courses):
    system.input_course()

  system.input_marks()

  system.list_courses()
  system.list_students()
  system.show_marks()

if __name__ == "__main__":
  main()