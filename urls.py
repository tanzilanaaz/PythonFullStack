from django.urls import path
from . import views


urlpatterns = [
    path('ems/', views.ems),
    path('g-emp/<pk>/', views.get_employee_by_id, name='get_employee'),
    path('u-emp/<pk>/', views.update_employee_by_id, name='update_employee'),
    path('d-emp/<pk>/', views.delete_employee_by_id, name='delete_employee'),
]

# http://localhost:8000/employee/ems/ -----> url to access emp related things