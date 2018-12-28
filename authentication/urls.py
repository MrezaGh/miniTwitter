from django.urls import path
from . import views


app_name = 'auth'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('profile/avatar', views.profile_avatar, name='profile_avatar'),
    path('profile/', views.profile, name='profile'),

]
