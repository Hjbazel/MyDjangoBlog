from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('Hi Hello World')
    return render(request,'about.html')

def home(request):
    # return HttpResponse('This is Home')
    return render(request,'home.html')
