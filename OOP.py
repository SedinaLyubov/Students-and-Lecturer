class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []
       
class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.lector_grades = {}
  
  def av_rating(self):
    for course in self.lector_grades.values():
      x = round(sum(course) / len(course), 2)
      return x  
      
  def av_rating_course(self, course):
    for x in self.lector_grades.keys():
      if x == course:
        res = round(sum(self.lector_grades[course]) / len(self.lector_grades[course]), 2)
    return res
    
  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print("Not Lecturer!")
      return
    return self.av_rating() < other.av_rating()

  def __str__(self):
    return (f"Лектор\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rating()}") 

class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}  
  
  def rate_lecture(self, lector, course, grade):
    if isinstance(lector, Lecturer):
      if course in lector.lector_grades:
        lector.lector_grades[course] += [grade]
      else:
        lector.lector_grades[course] = [grade]
    else:
      return 'Ошибка'

  def av_rating(self):
    for course in self.grades.values():
      x = round(sum(course) / len(course), 2)
      return x
      
  def av_rating_course(self, course):
    for x in self.grades.keys():
      if x == course:
        res = round(sum(self.grades[course]) / len(self.grades[course]), 2)
    return res
    
  def __lt__(self, other):
    if not isinstance(other, Student):
      print("Not Student!")
      return
    return self.av_rating() < other.av_rating()

  def __str__(self):
    return (f"Студент\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_rating()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)} ") 

class Reviewer(Mentor): 
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'

  def __str__(self):
    return (f"Ревьюер\nИмя: {self.name}\nФамилия: {self.surname}") 


#Students
best_student = Student('Ruoy', 'Eman', 'Male')
best_student.courses_in_progress += ['Python', 'Java']
best_student.finished_courses += ['Full-stack developer']

best_student_1 = Student('Emma', 'Po', 'Female')
best_student_1.courses_in_progress += ['Java', 'Python']
best_student.finished_courses += ['Git', 'Frontend-developer']

#Lecturer
some_best_lector = Lecturer('Zar', 'Eman')
some_best_lector_2 = Lecturer('Bin', 'Tall')

#Reviewer
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git', 'Full-stack developer']
cool_mentor_1 = Reviewer('Mary', 'Mint')
cool_mentor.courses_attached += ['Java', 'Frontend-developer', 'Python']

cool_mentor.rate_hw(best_student, 'Python', 5)
cool_mentor_1.rate_hw(best_student_1, 'Java', 10)
cool_mentor.rate_hw(best_student_1, 'Git', 5)
cool_mentor.rate_hw(best_student_1, 'Python', 3)
cool_mentor.rate_hw(best_student, 'Python', 5)

best_student.rate_lecture(some_best_lector_2, 'Python', 4)
best_student_1.rate_lecture(some_best_lector_2, 'Java', 10)
best_student_1.rate_lecture(some_best_lector, 'Python', 10)
best_student_1.rate_lecture(some_best_lector, 'Python', 3)

student_list = [best_student_1, best_student]
lector_list = [some_best_lector, some_best_lector_2]


def av_rating_course_students(course, student_list):
  x = 0
  y = 0
  for a in student_list:
    for b in a.grades:
      rate = a.av_rating_course(course)
      x += rate
      y += 1
  res = round(x/y, 2)
  return res

def av_rating_course_lecturer(course, lector_list):
  x = 0
  y = 0
  for a in lector_list:
    for b in a.lector_grades:
      rate = a.av_rating_course(course)
      x += rate
      y += 1
  res = round(x/y, 2)
  return res


print(f'Средняя оценка за домашние задания по курсу: {av_rating_course_students("Python", student_list)}')
print(f"Средняя оценка за лекции: {av_rating_course_lecturer('Python', lector_list)}")
print()
print('Студент01 < Студент02 ',best_student < best_student_1)
print('Лектор01 > Лектор02 ',some_best_lector > some_best_lector_2)
print()
print(f'{best_student}\n\n{best_student_1}')
print()
print(f'{some_best_lector}\n\n{some_best_lector_2}')
print()
print(f'{cool_mentor}\n\n{cool_mentor_1}')

