"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studut.views import clesses,student

urlpatterns = [
    path('classes',clesses.get_clesses),
    path('add_classes_data',clesses.add_classes_data),
    path('del_student_data',clesses.del_student_data),
    path('updata_student_Data',clesses.updata_student_Data),
    path('get_student',student.get_student),
    path('add_student',student.add_student),
    path('del_student',student.del_student),
    path('updata_student',student.updata_student)

]
