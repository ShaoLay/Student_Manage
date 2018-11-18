from django.shortcuts import render, redirect

from student import models


def get_classer(request):
    '''
    获取班级
    :param request:
    :return:
    '''
    cls_list = models.Classes.objects.all()
    return render(request, 'get_classes.html',{'cls_list':cls_list})

