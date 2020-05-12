from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from . models import Movie
from .forms import UserForm

# Create your views here.
def index(request):
    m = Movie.objects.all()
    context = {
        'm' : m,
    }
    return render(request, 'iflix/index.html', context)


def register(request):
    registered = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save
            registered = True
        return HttpResponseRedirect("/iflix/register/login")
    else:
        form = UserForm()
    return render(request, 'iflix/register.html', {'form' : form, 'registered' : registered })


def Userlogin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/iflix/review")
            else:
                return HttpResponse('Invalid Credentials')
        else:
            return HttpResponse('invalid Credentials')
    else:
        return render(request, 'iflix/login.html', {})


def review(request):
    movie = Movie.objects.all()
    context = {
        'movie' : movie,
    }
    return render(request, 'iflix/review.html', context)


def contact(request): 
    return render(request, 'iflix/contact.html',{})


def search(request):
    if request.method == 'GET':
        query =request.GET.get('q','')
        results = Movie.objects.filter(movie_name__icontains = query)
        context = {'results' : results,}
        return render(request, 'iflix/search.html', context)
    else:
        results = []
    return render(request, 'iflix/search.html',{})


def contact(request):
    return render(request, 'iflix/contact.html', {})