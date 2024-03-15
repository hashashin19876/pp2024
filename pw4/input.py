def input_student():
  id = input("Enter student id: ")
  name = input("Enter student name: ")
  dob = input("Enter student DoB: ")
  return Student(id, name, dob)

def input_course():
  id = input("Enter course id: ")
  name = input("Enter course name: ")
  credit = int(input("Enter course credit: "))
  return Course(id, name, credit)

def input_marks(system):
  course_id = input("Select a course by id: ")
  course_credit = next(course.credit for course in system.courses if course.id == course_id)
  for student in system.students:
    mark = float(input(f"Enter mark for student {student.name}: "))
    mark = math.floor(mark * 20) / 20  # round down to 1-digit decimal
    student.marks.append(mark)
    student.credits.append(course_credit)
    system.marks.append(Mark(student.id, course_id, mark))
