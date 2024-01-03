from django.shortcuts import render
from .models import Place

# Create your views here.
from django.http import HttpResponse
def demo(request):
    obj=Place.objects.all()
    return render (request,'index1.html',{'result':obj})
