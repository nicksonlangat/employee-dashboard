from django.shortcuts import render
from rest_framework import serializers
from .models import Employee
# Create your views here.

class EmployeeSerializer(serializers.ModelSerializer):
    pass

class EmployeeList(ListCreateApiView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer