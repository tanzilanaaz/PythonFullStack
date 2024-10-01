from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    contact_num = models.IntegerField()
    email_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    dob = models.DateField()
    courses = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
