class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year


class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

print(roger.name, roger.year)
print(sandro.name, sandro.year)
print(pieter.name, pieter.year)