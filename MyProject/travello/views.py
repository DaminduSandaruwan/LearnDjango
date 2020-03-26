from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def index(request):

    dests = Destination.objects.all()


    # Deleted Static content and connect to db
    """dest1 = Destination()
    dest1.name='Mumbai'
    dest1.desc= 'THe City that never Sleep'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name='Hyderabad'
    dest2.desc= 'Frist Buriyani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest2.offer=True

    dest3 = Destination()
    dest3.name='Bengaluru'
    dest3.desc= 'Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 800
    dest3.offer=False

    dests=[dest1,dest2,dest3]"""

    return render(request,'index.html',{'dests':dests})
    #return render(request,'index.html',{'dest1':dest1,'dest2':dest2,'dest3':dest3})
    #return render(request,'index.html',{'price':700}) # pass bali price
 