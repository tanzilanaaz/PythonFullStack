import json
from .models import Employee
from django.http import HttpResponse
from django.core.serializers import serialize


def employee_crud_api(request, pk=None):
    if request.method == 'POST':
        emp_input_json = request.body

        #2.Convert Employee JSON Data into Python Object
        emp_input_dict = json.loads(emp_input_json)

        #3. Extract Input Employee details from dict
        empid = emp_input_dict.get('empid')
        name = emp_input_dict.get('name')
        age = emp_input_dict.get('age')
        salary = emp_input_dict.get('salary')
        address = emp_input_dict.get('address')

        #4. create employee model
        employee = Employee(empid=empid, name=name, age=age, salary=salary,
                            address=address)

        #5. call save method
        employee.save()

        #6. prepare response object(dict) with success message
        message_dict = {'message': 'Employee created successfully'}

        #7. convert dict object into json using dumps()
        message_json = json.dumps(message_dict)

        #8. send json success response to client
        return HttpResponse(message_json, content_type="application/json")

    elif request.method == 'GET':
        if pk is not None:
            emp_db = Employee.objects.get(id=pk)
            # Step-1: Get employee details from db based on PK Value

            # Step-2: Convert employee model object into dict - Manually
            emp_dict = {
                'id': emp_db.id,
                'empid': emp_db.empid,
                'name': emp_db.name,
                'age': emp_db.age,
                'salary': emp_db.salary,
                'address': emp_db.address
            }

            # step-3: Convert employee dict object into JSON - dumps()
            emp_json = json.dumps(emp_dict)

            # step-4 send the json response back to the user/client
            return HttpResponse(emp_json, content_type='application/json')
        else:
            # Step-1: Get All employee from db based
            emps_db = Employee.objects.all() #data will be in the form of QuerySet

            # Step-2: Convert employee QS object into dict - serialize
            emps_json = serialize('json', emps_db)
            emps_json_parsed_data = parse_serialized_data(emps_json)

            # step-3 send the json response back to the user/client
            return HttpResponse(emps_json_parsed_data, content_type='application/json')

    elif request.method == 'PUT':
        # 1. Read input data - JSON
        emp_json = request.body

        # 2. JSON converted into dict
        emp_dict = json.loads(emp_json)

        # 3. Get existing employee data from DB - EmployeeDB Object
        emp_db = Employee.objects.get(id=pk)

        # 4. update employeeDB object with inputdata
        emp_db.empid = emp_dict.get('empid')
        emp_db.name = emp_dict.get('name')
        emp_db.age = emp_dict.get('age')
        emp_db.salary = emp_dict.get('salary')
        emp_db.address = emp_dict.get('address')

        # 5. call save method on employeeDB object
        emp_db.save()

        # 6. Create a Response dict object
        resp_dict = {'message': 'Employee updated successfully!!!'}

        # 7. Convert dict object into JSON
        resp_json = json.dumps(resp_dict)

        # 8. Send the JSON success response to the client
        return HttpResponse(resp_json, content_type="application/json")

    elif request.method == 'DELETE':
        # 1. Get existing employee data from DB - EmployeeDB Object
        emp_db = Employee.objects.get(id=pk)

        # 2. call delete method on employeeDB object
        emp_db.delete()

        # 3. Create a Response dict object
        resp_dict = {'message': 'Employee deleted successfully!!!'}

        # 4. Convert dict object into JSON
        resp_json = json.dumps(resp_dict)

        # 5. Send the JSON success response to the client
        return HttpResponse(resp_json, content_type="application/json")

def parse_serialized_data(emp_json_with_metadata):
    emp_dict_with_metadata = json.loads(emp_json_with_metadata)

    employee_list = []

    for emp_meta in emp_dict_with_metadata:
        employee = emp_meta['fields']
        employee['id'] = emp_meta['pk']
        employee_list.append(employee)

    return json.dumps(employee_list)



