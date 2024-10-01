# Try to modify Global variable from function
# Can we access local variable from other functions/other places of the script
# is it possible to have same name for Global Variable & Local Variable
'''
x = 50

z = 999

def f1():
    #x = x + 100
    y = 888
    z = 111
    print("I am inside f1()... x = ", x)
    print("I am inside f1()... Y = ", y)
    print("I am inside f1()... z = ", z)
def f2():
    print("I am inside f2()... x = ", x)
    #print("I am inside f2()... Y = ", y)
    print("I am inside f2()... z = ", z)


print("I am outside of functions...x = ", x)
#print("I am outside of functions...y = ", y)
print("I am outside of functions...z = ", z)


f1()
f2()
'''

# Try to modify Global variable from function

x = 50


def f1():
    global x
    x = x + 100
    print("I am inside f1()... x = ", x)


def f2():
    print("I am inside f2()... x = ", x)


print("I am outside of functions...x = ", x)

f1()
f2()