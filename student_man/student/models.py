from django.db import models

# Create your models here.


class Classes(models.Model):
    '''
    班级表
    '''
    title = models.CharField(max_length=32)
    a = models.ManyToManyField('Teachers')

class Teachers(models.Model):
    '''
    老师
    '''
    name = models.CharField(max_length=32)

class Students(models.Model):
    '''
    学生
    '''
    username = models.CharField(max_length=32)
    age = models.IntegerField(max_length=32)
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes, on_delete=models.CASEADE)
