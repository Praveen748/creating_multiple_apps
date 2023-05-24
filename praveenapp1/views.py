from django.shortcuts import render
from django.http import HttpRequest
def firstmap(request):
    return HttpRequest('hi this is praveen')


# Create your views here.
def temp1(request):
    return render(request,'temp1.html')
