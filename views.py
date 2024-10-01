from django.shortcuts import render

def fun(request):
    return render(request,"astiApp/test.html")