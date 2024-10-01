#Class Definition
"""
Always begin class name with capital Letter

class Classname():        the parentheses is optional
   "1. Description comment to describe why this class was created"
   2. Variables - Static Variables
   3. Constructor - Initializing Instance Variables
   4. Methods/Functions
"""


'''
class Test():
    """This is my first class"""
    # 2. Variables
    # 3. Constructor
    def __init__(self):
        print("Constructor Called")

    #4. Methods

    def m1(self):
        print("Method Called")

print("I am Outside the class 1")

t1 = Test()
t1.m1()

print("I am outside class 2")

'''

"""
class Employee():
    def __init__(self):
        print("Constructor Called")

    def get_emp_info(self):
        print("Method called")

print("I am outside the class")

emp1 = Employee()

print("The class is called but not method yet")

emp1.get_emp_info()

print("I am outside class after method is called")
"""

class Employee():
    def __init__(self):
        print("Constructor Called")
        self.empid = 1001
        self.name = "Tanu"
        self.age = 22
        self.address = "Dvg"

    def get_emp_info(self):
        print("Method Called")
        print("employee id = ", self.empid)
        print("name = ", self.name)
        print("age = ", self.age)
        print("address = ", self.address)

emp1 = Employee()

print("After object Created, Constructor Called, Method created but not yet called")

emp1.get_emp_info()

print("After Executing the Method called")

























































