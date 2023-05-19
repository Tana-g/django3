import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ormproject1.settings')
import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *
fake = Faker()

def populate(n):
    for i in range(n):
        feno = randint(101, 999)
        fename = fake.name()
        feaddr = fake.city()
        fesal = randint(10000,99999)
        emp_record = Employee.objects.get_or_create(
        eno = feno,
        ename = fename,
        eaddr = feaddr,
        esal = fesal)
n = int(input("enter no of employees:"))
populate(n)
print(f"{n}:no of record successfully stored.")
