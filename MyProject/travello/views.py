from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name='Mumbai'
    dest1.desc= 'THe City that never Sleep'
    dest1.img = 'destination_1.jpg'
    dest1.price = 7000

    dest2 = Destination()
    dest2.name='Sri Lanka'
    dest2.desc= 'Beautiful Country'
    dest2.img = 'destination_2.jpg'
    dest2.price = 456

    dest3 = Destination()
    dest3.name='Chaina'
    dest3.desc= 'Amazing Country'
    dest3.img = 'destination_3.jpg'
    dest3.price = 659

    dests=[dest1,dest2,dest3]

    return render(request,'index.html',{'dests':dests})
    #return render(request,'index.html',{'dest1':dest1,'dest2':dest2,'dest3':dest3})
    #return render(request,'index.html',{'price':700}) # pass bali price
 