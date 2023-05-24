from django.shortcuts import render
from django.http import HttpResponse

def app_String(request):
    return HttpResponse('This is returing string from app1')

def appWeb(request):
    return render(request,'app1.html')
# Create your views here.
