
def filter_adults(students: list[str, int]):
   return [student for student in students if student[1] >= 18]


people = [("Андрій", 25), ("Олег", 16), ("Марія", 19), ("Ірина", 15)]
print(filter_adults(people))