from django.urls import path

from . import views

urlpatterns = [
    path('' , views.qw1, name='qw1'),
    path('donat' , views.donat,name='donat'),
    path('qw', views.qw, name='qw'),

]