from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from api.models import TokenV1, TokenV2
from tweet.models import Tweet


def log_in(request):
    # tutorial: you need to send request like this: username=<your username> password=<your password>
    username = request.GET.get('username')
    password = request.GET.get('password')
    if username and password:
        user = authenticate(request, username=username, password=password)
        if not user:
            return HttpResponse("wrong username or password")
        # generate some random string
        token_hash = get_random_string(length=32)
        # if user already has a token remove it
        if hasattr(user, 'tokenv1'):
            print(user.username + "'s token was deleted and replaced")
            user.tokenv1.delete()
        # store the token in database with user
        token = TokenV1(key=token_hash, user=user)
        token.save()
        # token_hash_json = {'key': token.token}
        # send back the token_hash
        return HttpResponse(token.key)
    return HttpResponse('you did not input username and password')


def v1_tweet(request):
    # use token to find user
    token_hash = request.GET.get('key')
    if not token_hash:
        return HttpResponse('you did not send any key')
    try:
        token = TokenV1.objects.get(key=token_hash)
    except TokenV1.DoesNotExist:
        return HttpResponse('invalid key!')
    user = token.user
    # make tweet with request.GET and user and save it
    title = request.GET.get('title')
    content = request.GET.get('content')
    tweet = Tweet(title=title, content=content, user=user)
    tweet.save()
    return HttpResponse(tweet.title + " -- was created successfully")
    # return render(request, 'tweet/show_tweet.html', {'tweet': tweet})


def v2_generate_key(request):
    if not request.user.is_authenticated:
        return HttpResponse('you are not logged in')
    user = User.objects.get(pk=request.user.id)
    token_hash = get_random_string(length=32)
    # if user already has a token remove it
    if hasattr(user, 'tokenv2'):
        print(user.username + "'s token was deleted and replaced")
        user.tokenv2.delete()
    # store the token in database with user
    token = TokenV2(key=token_hash, user=user)
    token.save()
    # token_hash_json = {'key': token.token}
    # send back the token_hash
    return HttpResponse(token.key)


def v2_tweet(request):
    token_hash = request.GET.get('key')
    if not token_hash:
        return HttpResponse('you did not send any key')
    try:
        token = TokenV2.objects.get(key=token_hash)
    except TokenV2.DoesNotExist:
        return HttpResponse('invalid key!')
    user = token.user
    # make tweet with request.GET and user and save it
    title = request.GET.get('title')
    content = request.GET.get('content')
    tweet = Tweet(title=title, content=content, user=user)
    tweet.save()
    return HttpResponse(tweet.title + " -- was created successfully ")
