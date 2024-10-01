from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Course
from django.urls import reverse_lazy


class ListCourse(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course/list_course.html'
    success_url = reverse_lazy('list_course')


class CreateCourse(CreateView):
    model = Course
    fields = ('courseid', 'name', 'duration', 'faculty', 'mode')
    template_name = 'course/course_form.html'
    success_url = reverse_lazy('list_course')


class UpdateCourse(UpdateView):
    model = Course
    fields = ('courseid', 'name', 'duration', 'faculty', 'mode')
    template_name = 'course/course_update_form.html'
    success_url = reverse_lazy('list_course')
    context_object_name = 'course'


class DeleteCourse(DeleteView):
    model = Course
    context_object_name = 'course'
    # NOTE: By default Django will search for "employee_confirm_delete.html" template file,
    # if it is not present then error
    # template_name = 'cgvapp/employee_confirm_delete.html'
    success_url = reverse_lazy('list_course')

