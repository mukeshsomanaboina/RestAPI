import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pagination_project.settings')
import django
django.setup()

from testapp.models import Employee
from random import *
from faker import Faker
faker = Faker()

def populate(n):
    for i in range(n):
        feno = randint(101, 999)
        fename = faker.name()
        fesal = randint(25000, 50000)
        feaddr = faker.city()
        emp_records = Employee.objects.get_or_create(
            eno = feno,
            ename = fename,
            esal = fesal,
            eaddr = feaddr
        )
n = int(input('enter records:'))
populate(n)
print(f'{n} records inserted successfully')