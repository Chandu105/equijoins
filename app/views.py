from django.shortcuts import render
from django.db.models.functions import Length
from django.db.models import Q
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



def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='ALLEN',mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='KING',deptno__dname='ACCOUNTING')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(mgr__ename='BLAKE')|Q(deptno__dname='ACCOUNTING'))
    emd=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='K')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename__endswith='N')

    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').order_by('ename')
    emd=Emp.objects.select_related('deptno','mgr').order_by('-ename')
    emd=Emp.objects.select_related('deptno','mgr').order_by(Length('ename'))
    emd=Emp.objects.select_related('deptno','mgr').order_by(Length('ename').desc())
    emd=Emp.objects.select_related('deptno','mgr').order_by('mgr__ename')
    emd=Emp.objects.select_related('deptno','mgr').order_by('-mgr__ename')
    emd=Emp.objects.select_related('deptno','mgr').order_by(Length('mgr__ename'))
    emd=Emp.objects.select_related('deptno','mgr').order_by(Length('mgr__ename').desc())
    emd=Emp.objects.select_related('deptno','mgr').order_by('deptno__dname')
    emd=Emp.objects.select_related('deptno','mgr').order_by('-deptno__dname')
    emd=Emp.objects.select_related('deptno','mgr').order_by(Length('deptno__dname'))
    emd=Emp.objects.select_related('deptno','mgr').order_by(Length('deptno__dname').desc())
    emd=Emp.objects.select_related('deptno','mgr').exclude(ename__in=('ALLEN','SMITH','SCOTT','KING'))
    emd=Emp.objects.select_related('deptno','mgr').exclude(mgr__ename__in=('BLAKE','KING','CLARK'))
    emd=Emp.objects.select_related('deptno','mgr').exclude(deptno__dname__in=('SALES','RESEARCH','OPERATIONS'))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__endswith='K')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__startswith='K')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__endswith='G')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__startswith='R')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename__contains='ALLEN')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__contains='SALES')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__contains='KING')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname__contains='SALES')|Q(mgr__ename__contains='KING'))
   
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)



def emp_salgrade(request):
    #EO=Emp.objects.all()
    #SO=SalGrade.objects.all()
    SO=SalGrade.objects.filter(grade__in=(3,4))
    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))
    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)