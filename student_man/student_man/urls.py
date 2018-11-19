"""student_man URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from student.views import classes, students

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('classes.html', classes.get_classes),
    url('add_classes.html', classes.add_classes),
    url('del_classes.html', classes.del_classes),
    url('edit_classes.html', classes.edit_classes),

    url('students.html', students.get_students),
    url('add_students.html', students.add_students),
    url('del_students.html', students.del_students),
    url('edit_students.html', students.edit_students),
]
