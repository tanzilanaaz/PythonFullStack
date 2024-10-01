from django.db import models

# Create your models here.
class Course(models.Model):
    courseid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    faculty = models.CharField(max_length=100)
    mode = models.CharField(max_length=10)
