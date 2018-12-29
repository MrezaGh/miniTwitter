from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    path('v1/login', views.log_in, name='login_v1'),
    path('v1/tweet', views.v1_tweet, name='tweet_v1'),
    path('v2/tweet', views.v2_tweet, name='tweet_v2'),
    path('v2/generate_key', views.v2_generate_key, name='generate_key'),
]
