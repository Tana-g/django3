from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models import Avg,Max,Min,Sum,Count
from django.db.models.Function import lower
#from django.db.models import Create,Update,Delete
# Create your views here.
def retrive_view(request):
    #emp_list = Employee.objects.all().values_list('eno','ename')
    #emp_list = Employee.objects.filter(eno__range=[100,350]).values('eno','ename')
    #emp_list = Employee.objects.all().only('ename','esal')
    #emp_list = Employee.objects.all()
    #emp_list = Employee.objects.filter(esal__gte=85000)
    #emp_list = Employee.objects.filter(ename__iexact='VISHNU')
    #emp_list = Employee.objects.filter(eno__iexact=333)
#OR Operation
    #emp_list = Employee.objects.filter(ename__istartswith='t') | Employee.objects.filter(esal__gte=90000)
    #emp_list = Employee.objects.filter(Q(ename__istartswith='a') | Q(esal__range=[10000,13000]))
#AND Opration
    #emp_list = Employee.objects.filter(eaddr__istartswith='n') & Employee.objects.filter(eno__gte=785)
    #emp_list = Employee.objects.filter(Q(eaddr__iendswith='y') & Q(eno__lte=978))
    #emp_list = Employee.objects.filter(eaddr__iendswith='l',eno__lt=333)
#NOT Operation
    #emp_list = Employee.objects.filter(~Q(ename__istartswith='s'))
    #emp_list = Employee.objects.exclude(eaddr__iendswith='y')
    #emp_list = Employee.objects.filter(eaddr__iendswith='d')
    #emp_list =Employee.objects.filter(eaddr__in='manipal')
    #emp_list = Employee.objects.filter(ename__contains='VISHNU')
    #emp_list = Employee.objects.filter(esal__range=[10000,20000])
    #return render(request,'testapp/index.html',{'emp_list':emp_list})
#by using.values()
    #return render(request,'testapp/specificcolomns.html',{'emp_list':emp_list})
#by using only()
#by using sort function
    #emp_list = Employee.objects.all().order_by('eno')
    #emp_list = Employee.objects.all().order_by('-eno')
    #emp_list = Employee.objects.all().order_by('ename')
    #emp_list = Employee.objects.all().order_by('esal')
    #emp_list = Employee.objects.all().order_by('-esal')
    #emp_list = Employee.objects.all().order_by(('eaddr'))
    emp_list = Employee.objects.all().order_by(lower('eaddr'))
    #emp_list = Employee.objects.all().order_by(('-eaddr'))
#by create Data
    #emp_list = Employee.objects.create(eno=2222,ename="Narsimha",eaddr="telkaplly",esal=91258)
    return render(request,'testapp/index.html',{'emp_list':emp_list})

def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg':avg['esal__avg'],'max':max['esal__max'],'min':min['esal__min'],'sum':sum['esal__sum'],'count':count['esal__count']}
    return render (request,'testapp/aggregate.html', my_dict)
