"""
URL configuration for demopro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Goodmorning',views.Goodmorning.as_view(),name="Goodmorning"),
    path('Helloworld',views.Helloworld.as_view(),name="Helloworld"),
    path('Goodevening',views.Goodevening.as_view(),name="Goodevening"),
    path('Userdetails',views.Userdetails.as_view(),name="Userdetails"),
    path('Studentlist',views.Studentlist.as_view(),name="Studentlist"),
    path('StudentCreate',views.StudentCreate.as_view(),name="StudentCreate"),
    path('Studentdetail/<int:i>',views.Studentdetail.as_view(),name="Studentdetail"),
    path('Studentdelete',views.Studentdelete.as_view(),name="Studentdelete"),
]
