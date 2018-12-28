from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    context = {'loggedIn': False}
    if request.user.is_authenticated:
        context = {'loggedIn': True}
    return render(request, 'authentication/index.html', context)


def sign_up(request):
    if request.POST:
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])#todo: more clean?
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        #todo: handle errors
        return HttpResponseRedirect(reverse('auth:index'), {'message': 'you successfully signed up'})#todo: hpw to send a message?
    return render(request, 'authentication/sign_up.html')


def log_in(request):
    if request.POST:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('auth:profile'))
        else:
            return HttpResponseRedirect(reverse('auth:log_in'))
    return render(request, 'authentication/log_in.html')



def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth:index'))


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponse('hey hey, log in first')
    return render(request, 'authentication/profile.html')
