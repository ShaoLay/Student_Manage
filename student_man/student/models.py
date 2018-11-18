from django.db import models

# Create your models here.


class Classes(models.Model):
    '''
    班级表
    '''
    title = models.CharField(max_length=32)
    a = models.ManyToManyField('Teachers')

