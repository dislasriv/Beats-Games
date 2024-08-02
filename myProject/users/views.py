from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login 

# Create your views here.
def register(request):
    # If method post check if form valid, else return form with errors listed
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        #if valid save user and redirect
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")  
    #if method GET return default page
    else:
        form = UserCreationForm()

    #Renders register.html
    #Since form is not null no matter what, this will never throw a RuntimeException
    return render(request, 'users/register.html', {'form':form})



def login_view(request):
    #if POST check if login form is valud, if not break out of block and return error form
    if request.method == "POST":
      form = AuthenticationForm(data=request.POST)

      #if form is valid, try logging in
      if form.is_valid():
          login(request, form.get_user())
          return redirect("/")
      
    #if GET load page
    else:
        form = AuthenticationForm()

    #render login.html, will show errors if login was not valid
    return render(request, 'users/login.html', {'form':form})
