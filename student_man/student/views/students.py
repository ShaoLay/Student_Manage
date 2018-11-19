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