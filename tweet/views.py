from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'tweet/index.html')


def make_tweet(request):
    return HttpResponse('you are sending tweets, believe me')


def tweets(request):
    return HttpResponse('you are watching all the tweets')
