from django.http import HttpResponse
from .models import Employee
from .serializers import EmployeeSerializers
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCBV(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            emp_ser = EmployeeSerializers(emp)
            emp_json = JSONRenderer().render(emp_ser.data)
            return HttpResponse(emp_json, content_type='application/json')
        qs = Employee.objects.all()
        emp_ser = EmployeeSerializers(qs, many=True)
        emp_json = JSONRenderer().render(emp_ser.data)
        return HttpResponse(emp_json, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        serializer = EmployeeSerializers(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Resource created successfully.'}
            msg_json = JSONRenderer().render(msg)
            return HttpResponse(msg_json, content_type='application/json')
        msg_json = JSONRenderer().render(serializer.errors)
        return HttpResponse(msg_json, content_type='application/json', status=400)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        if id is None or id == '':
            msg = {'msg': 'Please provide valid id for updation.'}
            msg_json = JSONRenderer().render(msg)
            return HttpResponse(msg_json, content_type='application/json')
        emp = Employee.objects.get(id=id)
        print(emp)
        serializer = EmployeeSerializers(emp, data=pdata, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Resource Updated successfully.'}
            msg_json = JSONRenderer().render(msg)
            return HttpResponse(msg_json, content_type='application/json')
        msg_json = JSONRenderer().render(serializer.errors)
        return HttpResponse(msg_json, content_type='application/json', status=400)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        if id is None:
            msg = {'msg': 'Please provide valid id for delete resource.'}
            msg_json = JSONRenderer().render(msg)
            return HttpResponse(msg_json, content_type='application/json')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg': 'Resource deleted successfully.'}
        msg_json = JSONRenderer().render(msg)
        return HttpResponse(msg_json, content_type='application/json')
