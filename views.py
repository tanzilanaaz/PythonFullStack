from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def contact_us(request):
    return render(request, "contactus.html")

def about_us(request):
    return render(request, "aboutus.html")