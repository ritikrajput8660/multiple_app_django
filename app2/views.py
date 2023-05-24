from django.shortcuts import render
from django.http import HttpResponse

def app_String2(request):
    return HttpResponse('This is returing string from app1')

def appWeb2(request):
    return render(request,'app2.html')
# Create your views here.
