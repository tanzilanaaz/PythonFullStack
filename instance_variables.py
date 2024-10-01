#methods to declare instance variables

class Test:
    def __init__(self, eid, ename):
        print("This is Constructor")
        # 1. inside a constructor
        self.id = eid
        self.name = ename
        self.x = 20

    def im(self, eage):
        print("This is instance method")
        # 2. inside a instance method
        self.age = eage

    @classmethod
    def cm(cls):
        print("This is class method")

    @staticmethod
    def sm():
        print("This is static method")

t = Test(1001, "Tanu")
print("The contents of t are = ", t.__dict__)

t.im(22)
print("The contents of t after calling instance method are = ", t.__dict__)

# 3. outside the class
t.d = 30
print("The contents of t after declaring d are = ", t.__dict__)


print("=====================================================================================")

#deletion of instance variables

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m(self):
        del self.b
t1 = Test()
print("Before delete Data present in t1 = ", t1.__dict__)
t1.m()
print("After delete Data present in t1 = ", t1.__dict__)

t2 = Test()
print("Before delete Data present in t2 = ", t2.__dict__)
del t2.a, t2.b
print("After delete Data present in t2 = ", t2.__dict__)
