from django.http import HttpResponse

def homePage(request):
    return HttpResponse("Hello World!")

def about(request):
    return HttpResponse("information about my page: creator is human waste!")
