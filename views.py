from django.shortcuts import render
from . models import Student
from django.http import HttpResponse


'''
1. Read Student form input data
2. From above input data Create a Student Model object
3. by Using Student model object call save() method to insert Student data into Postgres Database
4. Send the response back to the user saying that Student created successfully.
'''


def create_student(request):
    if request.method == 'GET':
        return render(request, 'studentapp/student_form.html')
    elif request.method == 'POST':
        #1. Reading the inputs from student form
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        contact_num = request.POST.get("contact_num")
        email_id = request.POST.get("email_id")
        city = request.POST.get("city")
        state = request.POST.get("state")
        address = request.POST.get("address")
        dob = request.POST.get("dob")
        python = request.POST.get("python")
        java = request.POST.get("java")
        net = request.POST.get("net")
        bigdata = request.POST.get("bigdata")
        datascience = request.POST.get("datascience")
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")

        courses = python + ", " + java + ", " + net + ", " + bigdata + ", " + datascience

        #2. create a student object using above input data
        student = Student(first_name=first_name, last_name=last_name, gender=gender, contact_num=contact_num, email_id=email_id, city=city, state=state, address=address, dob=dob, courses=courses, user_name=user_name, password=password)

        #3. call save method of student model object to insert student data into the database
        student.save()

        #4. return success response to the user
        return HttpResponse("Student Created Successfully")


def student_list(request):
    #1. get all details from database
    students_db = Student.objects.all()

    #2. with list of students, construct a context object
    student_context = {
        "students": students_db,
    }

    # Step-3: Sent student context object to student_list.html'
    return render(request, "studentapp/student_list.html", context=student_context)

