from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
#
# def first(request):
#     return HttpResponse("First page")
# def second(request):
#     return HttpResponse("Second page")
from django.views import View
class First(View):
    def get(self,request):
        return HttpResponse("First Page")
class Second(View):
    def get(self,request):
        return HttpResponse("Second Page")