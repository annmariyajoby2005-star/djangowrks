

#create your view
from django.shortcuts import render
from django.views import View
from books.models import Book



class Home(View):
    def get(self,request):
        return render(request,'home.html')
class View_book(View):
    books=Book.object.all()
    context={'books':books}
    return render(request,viewbook.html,context)
class AddBook(View):
    def get(selfself,request):
        return render(request,'addbook.html')
    def post(selfself,request):
        data=request.POST
        t=data['title']
        a=data['auyhor']
        p=data['price']
        l=data['language']
        pa=data['pages']
        b=Book.objects.create(title=t,author=a,price=p,language=l,pages=pa)
        return render(request,'addmovie.html')
# Create your views here.
