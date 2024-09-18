from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loading(request):
    return render(request, "index.html")

def register(request):

    if request.method =="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "your account have been successfully creat.")
        return redirect('login')

    return render(request, "register.html")

def login(request):

    if request.method == "POST":
        username = request.POST.get('username') 
        pass1 = request.POST.get('pass1')

        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.error(request, "login successfully")
            return redirect('home')


    return render(request, "login.html")

 
def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def index_2(request):
    return render(request, "index-2.html")

def movie(request):
    return render(request, "movie.html")

def movie_details(request):
    return render(request, "movie-details.html")

def tv_show(request):
    return render(request, "tv-show.html")

def pricing(request):
    return render(request, "pricing.html")

def blog(request):
    return render(request, "blog.html")

def blog_details(request):
    return render(request, "blog-details.html")

def contact(request):
    return render(request, "contact.html")

def logout(request):
    auth.logout(request)
    return redirect('home')

