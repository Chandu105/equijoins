from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='DALLAS')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gt=2000)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=1981,comm__gt=100,deptno=30)
    EMPOBJECTS=Emp.objects.select_related('deptno').order_by('sal')
    EMPOBJECTS=Emp.objects.select_related('deptno').order_by('-sal')
    EMPOBJECTS=Emp.objects.select_related('deptno').order_by(Length('ename'))
    EMPOBJECTS=Emp.objects.select_related('deptno').order_by(Length('ename').desc())
    EMPOBJECTS=Emp.objects.select_related('deptno').exclude(deptno=30)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__month=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__day=8)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__startswith='S')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__endswith='H')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__in=('SMITH','SCOTT','MARTIN'))
    

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)


def selfjoins(request):
    empmgrobject=Emp.objects.select_related('mgr').all()
    empmgrobject=Emp.objects.select_related('mgr').filter(ename='MARTIN')
    empmgrobject=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    empmgrobject=Emp.objects.select_related('mgr').filter(sal__gte=2000)
    empmgrobject=Emp.objects.select_related('mgr').filter(sal__lte=3000)
    empmgrobject=Emp.objects.select_related('mgr').filter(ename__startswith='S')
    empmgrobject=Emp.objects.select_related('mgr').filter(ename__endswith='N')
    empmgrobject=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    empmgrobject=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    empmgrobject=Emp.objects.select_related('mgr').order_by('sal')
    empmgrobject=Emp.objects.select_related('mgr').order_by('-sal')
    empmgrobject=Emp.objects.select_related('mgr').order_by(Length('ename'))
    empmgrobject=Emp.objects.select_related('mgr').order_by(Length('ename').desc())
    empmgrobject=Emp.objects.select_related('mgr').filter(ename__in=('CLARK','ALLEN','JONES'))
    






    d={'empmgrobject':empmgrobject}
    return render(request,'selfjoins.html',d)