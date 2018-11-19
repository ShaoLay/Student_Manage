from django.shortcuts import render, redirect

from student import models


def get_students(request):
    '''
    获取学生
    :param request:
    :return:
    '''
    stu_list = models.Students.objects.all()
    return render(request, 'get_students.html', {'stu_list': stu_list})

def add_students(request):
    '''
    添加学生
    :param request:
    :return:
    '''
    if request.method=='GET':
        cs_list=models.Classes.objects.all()
        return render(request,'add_students.html',{'cs_list':cs_list})
    elif request.method=='POST':
        u=request.POST.get('username','')
        a=request.POST.get('age','')
        g=request.POST.get('gender','')
        c=request.POST.get('cs','')
        models.Students.objects.create(
        username=u,
        age=a,
        gender=g,
        cs_id=c
        )
        return redirect('/students.html')