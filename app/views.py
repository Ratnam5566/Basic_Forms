from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def Forms(request):
    if request.method=='POST':
        Name=request.POST ['N']
        City=request.POST ['C']
        print(Name)
        print(City)
        return HttpResponse('Data Is Submitted')


    return render (request,'Forms.html')
    
 
 