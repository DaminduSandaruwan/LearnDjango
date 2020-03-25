from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name='Mumbai'
    dest1.desc= 'THe City that never Sleep'
    dest1.price = 7000

    return render(request,'index.html',{'dest1':dest1})
    #return render(request,'index.html',{'price':700}) # pass bali price
 