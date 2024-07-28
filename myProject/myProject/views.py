#from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    #return HttpResponse("Hello World!")
    return render(request, "home.html")

def about(request):
    #return HttpResponse("information about my page: creator is human waste!")
    return render(request, "about.html")