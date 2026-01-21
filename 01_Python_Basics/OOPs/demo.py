## Create the user-defined class with some attributes and methods
"""
class Employee:
    ename = "Bhupendra"
    salary = 100000

    def display(self):
        print("Welcome to Method Concept")
        print("Employee Name is :", self.ename)
        print("Employee Salary is :", self.salary)


## Object creation for Employee class
emp = Employee()
emp.display()
"""

"""
class Employee:
    ## class variables
    ename = "Bhupendra"
    salary = 100000

    def display(self):
        print("Employee Name is :", Employee.ename)
        print("Employee Salary is :", Employee.salary)
        print()

        print("Employee Name is :", emp.ename)
        print("Employee Salary is :", emp.salary)
        print()

        print("Employee Name is :", self.ename)
        print("Employee Salary is :", self.salary)


## Object creation for Employee class
emp = Employee()
emp.display()

print("====================OUTSIDE Class =============================")
print("Employee Name is :", Employee.ename)
print("Employee Salary is :", Employee.salary)
print()

print("Employee Name is :", emp.ename)
print("Employee Salary is :", emp.salary)
print()

# print("Employee Name is :", self.ename)
# print("Employee Salary is :", self.salary)  ## NameError: name 'self' is not defined
"""

"""
### How to send the values to method parameters 
class Employee:
    def create(self, ename, salary):
        ##  instance variables
        self.ename = ename
        self.salary = salary

    def display(self):
        print("Employee Name is :", self.ename)
        print("Employee Salary is :", self.salary)

emp = Employee()
emp.create("Rahul", 300000)
emp.display()
"""