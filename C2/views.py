from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import  HttpResponse
from .models import Worker

def qw(request):
    return render(request , '12im.html')
#,{'h1':h1}
def qw1(request):
    return render (request, '13im.html')
def donat (request):
    return render(request,'14.html')
