from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_student),
    path('student-list/', views.student_list),
]