
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wish/', views.wish),
    path('home/', views.msg),
    path('res/', views.add_num),
    path('calculator/', views.calculator),
    path('login/', views.login),
    path("app1/", include("app1.urls")),
]
