from django.db.models import Model
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
class Goodmorning(View):
    def get(self,request):
        data={"message":"Goodmorning"}
        return JsonResponse(data)
class Helloworld(View):
    def get(self,request):
        data = {"message": "Helloworld"}
        return JsonResponse(data)
class Goodevening(View):
    def get(self,request):
        data = {"message": "Goodevening"}
        return JsonResponse(data)
class Userdetails(View):
    def get(self,request):
        data = [{"name": "arum","age":23,"place":"ekm"},
                {"name": "amal","age":24,"place":"tvm"},
                {"name": "anu","age":25,"place":"knr"}]
        return JsonResponse(data,safe=False)

from myapp.models import Student
class Studentlist(View):
    def get(self,request):
        s = Student.objects.all()
        print(s)
        print(type(s))

        s=Student.objects.all().values()
        print(s)
        print(type(s))
        data=list(s)
        print(data)
        print(type(data))
        return JsonResponse(data,safe=False)

from json import loads
@method_decorator (csrf_exempt,name="dispatch")
class StudentCreate(View):
    def post(self,request):
        data=loads(request.body)
        r=data['rollno']
        n=data['name']
        a=data['age']
        p=data['place']
        m=data['marks']
        s=Student.objects.create(rollno=r,name=n,age=a,place=p,marks=m)
        s.save()
        return JsonResponse({"message":"inserted data sucessfull"})

class Studentdetail(View):
    def get(self,request,i):
        s=list(Student.objects.filter(id=i).values())
        if s:
            return JsonResponse(s,safe=False)
        else:
            return JsonResponse({"message":"no student data"})
class Studentdelete(View):
    def delete (self,request,i):
        s=Student.objects.get(id=i)
        s.delete()
        return JsonResponse({"message": "deleted successfully"})


