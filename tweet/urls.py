from django.urls import path
from . import views


app_name = 'tweet'
urlpatterns = [
    path('', views.index, name='index'),
    path('make_tweet', views.make_tweet, name='make_tweet'),
    path('tweets', views.tweets, name='tweets'),
    path('<int:tweet_id>', views.show_tweet, name='show_tweet'),
]
