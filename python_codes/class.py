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

print("List students after sorting:\n%5s %5s %5s %5s %5s" % ("Name", "|", "Age", "|", "Test score"))
students.sort(key = lambda x: x.name)
for student in students:
    print( "%5s %5s %5d %5s %5.1f" % (student.name, "|", student.age, "|", student.testScore) )