"""In settings.py, base represents the root folder"""

# there are 2 types of views : 1. functional views 2. class views)

#functional views
from django.http import HttpResponse
from django.shortcuts import render


def wish(request):
    message = "Hello, Good Morning"
    return HttpResponse(message)


def msg(request):
    msg = "<h1 style = color:Red >Hi, Welcome</h1>"
    return HttpResponse(msg)


def add_num(request):
    x = 10
    y = 20
    res = ("The sum of {}, {} is {}".format(x, y, x + y))
    return HttpResponse(res)


def calculator(request):
    if request.method == 'GET':
        return render(request, 'test.html')
    elif request.method == 'POST':
        # Read first number
        first_num = int(request.POST.get("first_num"))

        # Read Second number
        second_num = int(request.POST.get("second_num"))

        # Read Operation
        Operation = request.POST.get("Operation")

        result = 0

        if Operation == "addition":
            result = first_num + second_num
        elif Operation == "subtraction":
            result = first_num - second_num
        elif Operation == "multiplication":
            result = first_num * second_num
        elif Operation == "division":
            result = first_num / second_num

        data = {
            "first_num": first_num,
            "second_num": second_num,
            "Operation": Operation,
            "result": result
        }
        return render(request, 'test.html', context=data)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        userId = 'Ali'
        password = 'ali123'

        userId_input = request.POST.get("userId")
        password_input = request.POST.get("password")

        if userId == userId_input and password == password_input:
            message = "Login is successful. Welcome {}".format(userId_input)
        else:
            message = "Login is unsuccessful with user id {}".format(userId_input)

        context_data = {
            "message": message
        }
        return render(request, 'login.html', context=context_data)