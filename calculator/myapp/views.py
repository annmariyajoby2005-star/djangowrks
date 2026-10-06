from django.shortcuts import render


# Create your views here.
from django.views import View
class Home(View):
    def get(self,request):
        return render(request,'Home.html')
class Add(View):
    def get(self, request):
        return render(request, 'Add.html')
    def post(self,request):
        data=request.POST
        num1=int(data['num1'])
        num2=int(data['num2'])
        s=num1+num2
        print(s)
        context={'result':s}
        return render(request, 'add.html',context)
class Fact(View):
    def get(self, request):
        return render(request, 'Fact.html')

    def post(self, request):
        data = request.POST
        num = int(data['num'])
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        context = {'fact': fact}
        return render(request, 'Fact.html', context)
class BMI(View
        ):
    def get(self, request):
        return render(request, 'bmi.html')
    def post(self, request):
        data = request.POST
        weight= int(data['weight'])
        height = int(data['height'])
        bmi=weight/(height*height)
        context = {'bmi': bmi}
        return render(request, 'bmi.html', context)

#api views for creating a new record
#
# class EmployeeCreate(APIView):
#     def post(self,request):
#         #View receives data as a request.data(client side data -python native type)
#         #Calls Serializer class for deserialization.here we pass request.data as argument
#         #after validation serializer saves data as model object inside db table
#
#     serializer_instance=EmployeeSerializer(data=request.data)
#     if serializer_instance.is_valid():
#         serializer_instance.save()
#         return Response({"mesege":"created"})
#     else:
#         return Response(serializer_instance.errors)
#

class EmployeeDetailCreate(APIView):
    def get(self,request,i):
        e=Employee.objects.get(id=i)
        #View receives data as a request.data(client side data -python native type)
        #Calls Serializer class for deserialization.here we pass request.data as argument
        #after validation serializer saves data as model object inside db table

        serializer_instance=EmployeeSerializer(e)

        return Response(serializer_instance.data)

class EmployeeDetailCreate(APIView):
    def get(self,request):
        e=Employee.objects.get(id=i)
        e.delete()
        return Response({"messege":"deleted"})