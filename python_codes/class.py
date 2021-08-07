class Student:
    def __init__(self, name, age, testScore):
        self.name = name
        self.age = age
        self.testScore = testScore

# Main
students = []
cnt = 3
while cnt > 0:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    testScore = float(input("Enter test score: "))
    students.append( Student(name, age, testScore)) 
    cnt-=1

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

# example:
'''
Enter name: Phuc
Enter age: 21
Enter test score: 3.2
Enter name: Phuc
Enter age: 21
Enter test score: 2.6
Enter name: Hoang
Enter age: 21
Enter test score: 8.0
List students before sorting:
 Name     |   Age     | Test score
 Phuc     |    21     |   3.2
 Phuc     |    21     |   2.6
Hoang     |    21     |   8.0
List students after sorting by name:
 Name     |   Age     | Test score
Hoang     |    21     |   8.0
 Phuc     |    21     |   3.2
 Phuc     |    21     |   2.6
List students after sorting by name and test score:
 Name     |   Age     | Test score
Hoang     |    21     |   8.0
 Phuc     |    21     |   2.6
 Phuc     |    21     |   3.2
'''