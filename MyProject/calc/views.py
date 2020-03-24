from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name' : 'Damindu'})
    #return render(request,'home.html')

    #return HttpResponse("<h1>Hello World</h1>")
   


