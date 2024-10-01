from django.shortcuts import render, redirect
from .models import Employee


def ems(request):
    if request.method == 'GET':
        # 1. get all details from database
        emps_db = Employee.objects.all()

        # 2. construct a context object
        emp_context = {
            "employees": emps_db,
        }
        return render(request, 'empapp/ems.html', context=emp_context)
    elif request.method == 'POST':
        #1. read the employee input data
        emp_empid = request.POST.get('emp_empid')
        name = request.POST.get('emp_name')
        age = request.POST.get('emp_age')
        salary = request.POST.get('emp_salary')
        address = request.POST.get('emp_address')
        doj = request.POST.get('emp_doj')
        designation = request.POST.get('emp_designation')

        #2. create a employee object using above input data
        employee = Employee(empid=emp_empid, name=name, age=age, salary=salary,
                            address=address, doj=doj, designation=designation)

        #3. call save method of student model object to insert student data into the database
        employee.save()

        #4. return success response to the client
        return redirect('/employee/ems/')


def get_employee_by_id(request, pk):
    return redirect('/employee/ems/')


def update_employee_by_id(request, pk):
    #step1: get details from db based on pk
    employee_db = Employee.objects.get(id=pk)

    #step2: update the details based on input values
    employee_db.empid = request.POST.get("emp_empid")
    employee_db.name = request.POST.get("emp_name")
    employee_db.age = request.POST.get("emp_age")
    employee_db.salary = request.POST.get("emp_salary")
    employee_db.address = request.POST.get("emp_address")
    employee_db.doj = request.POST.get("emp_doj")
    employee_db.designation = request.POST.get("emp_designation")

    #step3: call save method to update latest values
    employee_db.save()

    #step4: redirect to ems page
    return redirect('/employee/ems/')


def delete_employee_by_id(request, pk):
    # step1: get details from db based on pk
    employee_db = Employee.objects.get(id=pk)

    # step2: call delete method  on employee object
    employee_db.delete()

    # step3 : redirect request to employee ems page
    return redirect('/employee/ems/')
