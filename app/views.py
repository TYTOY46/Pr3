from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import  HttpResponse
from .models import Worker

def qw(request):
    return render(request , 'files_html\donat.html')
def qw1(request):
    return render (request , 'files_html\main_page.html')
def donat (request):
    return render(request,'files_html\workers.html')


