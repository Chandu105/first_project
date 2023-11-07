from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jampandu(request):
    return HttpResponse('<h1><marquee>welcome to django programming<marquee><h1>')
def chandana(request):
    return HttpResponse('<h1><marquee>i am going to do django programs here <marquee><h1>')