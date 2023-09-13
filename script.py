class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) is Grade:
      return self.grades.append(grade)
  
  def get_avg(self):
    curr = 0
    i=0
    for grade in self.grades:
      curr+=grade
      i+=1
    avg = curr/i
    return avg


class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self):
    if self.score >= self.minimum_passing:
        return True

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

print(roger.name, roger.year)
print(sandro.name, sandro.year)
print(pieter.name, pieter.year)

new_grade = Grade(100)
pieter.add_grade(new_grade)
print(pieter.grades)
not_grade = 100
sandro.add_grade(not_grade)
print(sandro.grades)