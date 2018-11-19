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

def add_classed(request):
    '''
    添加班级
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'add_classes.html')
    elif request.method == 'POST':
        title = request.POST.get('title','')
        models.Classes.objects.create(title=title)
        return redirect('/classes.html')

def del_classes(request):
    '''
    删除班级
    :param request:
    :return:
    '''
    nid = request.GET.get('nid','')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/classes.html')


