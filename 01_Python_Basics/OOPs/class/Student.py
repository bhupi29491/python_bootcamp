class Student:
    college_name = "SKP Engineering College"    #class attributes

    def __init__(self, name, cgpa):
        self.name = name    #instance attributes
        self.cgpa = cgpa

stud1 = Student('Bhupendra', 9.2)

print(Student.college_name)
print(stud1.name)
print(stud1.cgpa)
