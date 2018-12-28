from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from tweet.models import Tweet


# Create your views here.
def index(request):
    return render(request, 'tweet/index.html')


def make_tweet(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('auth:log_in'))
    if request.POST:
        tweet = Tweet(title=request.POST['title'], content=request.POST['content'], user=request.user)
        tweet.save()
        return HttpResponseRedirect(reverse('tweet:show_tweet', args=(tweet.id, )))
    return render(request, 'tweet/make_tweet.html')


def tweets(request):
    tweets_array = Tweet.objects.all()
    return render(request, 'tweet/all_tweets.html', {'tweets': tweets_array})


def show_tweet(request, tweet_id):
    tweet = Tweet.objects.get(pk=tweet_id)
    return render(request, 'tweet/show_tweet.html', {'tweet': tweet})
