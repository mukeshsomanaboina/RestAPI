from django.shortcuts import render
from rest_framework import viewsets
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeCRUDCBV(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    
