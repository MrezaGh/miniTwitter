from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.utils.crypto import get_random_string
from api.models import Token
from tweet.models import Tweet


def log_in(request):
    # tutorial: you need to send request like this: username=<your username> password=<your password>
    username = request.GET.get('username')
    password = request.GET.get('password')
    if username and password:
        user = authenticate(request, username=username, password=password)
        # generate some random string
        token_hash = get_random_string(length=32)
        # if user already has a token remove it
        if hasattr(user, 'token'):
            # print(user.username + "'s token was deleted and replaced")
            user.token.delete()
        # store the token in database with user
        token = Token(key=token_hash, user=user)
        token.save()
        # token_hash_json = {'key': token.token}
        # send back the token_hash
        return HttpResponse(token.key)
    return HttpResponse('you are logging in with api')


def v1_tweet(request):
    print(request.GET)
    # todo: use token to find user
    token_hash = request.GET.get('key')
    if not token_hash:
        return HttpResponse('you did not send any key')
    try:
        token = Token.objects.get(key=token_hash)
    except Token.DoesNotExist:
        return HttpResponse('invalid key!')
    user = token.user
    # todo: make tweet with request.GET and user and save it
    title = request.GET.get('title')
    content = request.GET.get('content')
    tweet = Tweet(title=title, content=content, user=user)
    tweet.save()
    return HttpResponse(tweet.title + " -- was created successfully")
    # return render(request, 'tweet/show_tweet.html', {'tweet': tweet})


def v2_tweet(request):
    return HttpResponse('tweet with v2')
