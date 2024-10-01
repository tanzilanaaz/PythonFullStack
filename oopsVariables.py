'''
Static variables are class level variables. they are declared just below class keyword line, outside of constructor and method
value of static variable doesn't change obj to obj
'''

#STATIC VARIABLES( Diff places to declare)

class Student:
    """ This is demo class of Static Variables """
    # 1. inside the class level obj
    college_name = "Crescent Engineering College"

    def __init__(self, sid, sname):
        # 2. inside the constructor
        Student.college_address = "Blr"
        self.id = sid
        self.name = sname

    def im(self):
        # 3. inside the instance method
        print("This is instance method")
        Student.college_ph = 1234

    @classmethod
    def cm(cls):
        # 4. inside the class method (1. by using class name and 2. by using cls)
        print("This is Class Method")
        Student.college_email1 = "cec@gmail.com"
        cls.college_email2 = "cec2@gmail.com"

    @staticmethod
    def sm():
        # 5. inside static method
        print("This is Static Method")
        Student.hod = "Prasad"

s1 = Student(1001,"Tanu")

s1.im()

s1.cm()

s1.sm()

# 6. outside the class
Student.hod2 = "Ravi"

print("What is there in Class Level Object???", Student.__dict__)