from django.urls import path
from . import views


urlpatterns = [
    path('employee/', views.employee_crud_api),
    path('employee/<pk>/', views.employee_crud_api),
]