import math
import numpy as np

class Student:
  def __init__(self, id, name, dob):
    self.id = id
    self.name = name
    self.dob = dob
    self.marks = []
    self.credits = []

  def __str__(self):
    return f"Student ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

  def calculate_gpa(self):
    weighted_marks = np.array(self.marks) * np.array(self.credits)
    return sum(weighted_marks) / sum(self.credits)
''
class Course:
  def __init__(self, id, name, credit):
    self.id = id
    self.name = name
    self.credit = credit

  def __str__(self):
    return f"Course ID: {self.id}, Name: {self.name}, Credit: {self.credit}"
  
class Mark:
  def __init__(self, student_id, course_id, mark):
    self.student_id = student_id
    self.course_id = course_id
    self.mark = mark

  def __str__(self):
    return f"Student ID: {self.student_id}, Course ID: {self.course_id}, Mark: {self.mark}"
  
