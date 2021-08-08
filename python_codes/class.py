class Student:
    def __init__(self, name, age, testScore):
        self.name = name
        self.age = age
        self.testScore = testScore

# Main
students = []

# Create students
students.append(Student('Phuc', 21, 3.2))
students.append(Student('Huy', 21, 8.0))
students.append(Student('Nam', 21, 6.7))
students.append(Student('Phuc', 21, 2.6))

print("List students before sorting:\n%5s %5s %5s %5s %5s" % ("Name", "|", "Age", "|", "Test score"))
for student in students:
    print( "%5s %5s %5d %5s %5.1f" % ( student.name, "|", student.age, "|", student.testScore) )

# sort by name
print("List students after sorting by name:\n%5s %5s %5s %5s %5s" % ("Name", "|", "Age", "|", "Test score"))
students.sort(key = lambda x: x.name)
for student in students:
    print( "%5s %5s %5d %5s %5.1f" % (student.name, "|", student.age, "|", student.testScore) )

# sort by name, if 2 students have same name, sort by their test score
print("List students after sorting by name and test score:\n%5s %5s %5s %5s %5s" % ("Name", "|", "Age", "|", "Test score"))
students.sort(key = lambda x: (x.name, x.testScore))
for student in students:
    print( "%5s %5s %5d %5s %5.1f" % (student.name, "|", student.age, "|", student.testScore) )

# sort by name and test score, but in descending
print("List students after sorting by name and test score in descending order:\n%5s %5s %5s %5s %5s" % ("Name", "|", "Age", "|", "Test score"))
students.sort(key = lambda x: (x.name, x.testScore), reverse = True)
for student in students:
    print( "%5s %5s %5d %5s %5.1f" % (student.name, "|", student.age, "|", student.testScore) )

# example:
'''
List students before sorting:
 Name     |   Age     | Test score
 Phuc     |    21     |   3.2
  Huy     |    21     |   8.0
  Nam     |    21     |   6.7
 Phuc     |    21     |   2.6

List students after sorting by name:
 Name     |   Age     | Test score
  Huy     |    21     |   8.0
  Nam     |    21     |   6.7
 Phuc     |    21     |   3.2
 Phuc     |    21     |   2.6

List students after sorting by name and test score:
 Name     |   Age     | Test score
  Huy     |    21     |   8.0
  Nam     |    21     |   6.7
 Phuc     |    21     |   2.6
 Phuc     |    21     |   3.2

List students after sorting by name and test score in descending order:
 Name     |   Age     | Test score
 Phuc     |    21     |   3.2
 Phuc     |    21     |   2.6
  Nam     |    21     |   6.7
  Huy     |    21     |   8.0
'''