#To enter data dynamically instead of hard coding


class Employee():

    def __init__(self, id, name, age, address):
        print("Constructor Called")
        self.id = id
        self.name = name
        self.age = age
        self.address = address

    def get_emp_info(self):
        print("Method called")
        print("Employee Id = ", self.id)
        print("Employee Name = ", self.name)
        print("Employee Age = ", self.age)
        print("Employee Address = ", self.address)


print("I am outside the class")

emp1 = Employee(1001, "Tanu", 22, "Dvg")
emp1.get_emp_info()
print("------------------------------------------------------")
emp2 = Employee(1002, "Panu", 23, "Mys")
emp2.get_emp_info()
print("------------------------------------------------------")
emp3 = Employee(1003, "Kanu", 24, "Blr")
emp3.get_emp_info()
print("------------------------------------------------------")
emp4 = Employee(1004, "Ganu", 25, "Hyd")
emp4.get_emp_info()
print("------------------------------------------------------")
