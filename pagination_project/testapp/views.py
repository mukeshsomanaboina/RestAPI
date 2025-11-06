from django.shortcuts import render
from rest_framework.generics import ListAPIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from testapp.pagination import MyPagination3


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination3



