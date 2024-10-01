from django.urls import path
from . import views

urlpatterns = [
    path('list_course/', views.ListCourse.as_view(), name="list_course"),
    path('add_course/', views.CreateCourse.as_view(), name="add_course"),
    path('update_course/<pk>/', views.UpdateCourse.as_view(), name='update_course'),
    path('delete_course/<pk>/', views.DeleteCourse.as_view(), name='delete_course'),
]
