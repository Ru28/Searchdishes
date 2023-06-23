from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    restaurants=Restaurants.objects.all()
    context={'restaurants':restaurants}
    return render(request,'index.html',context)