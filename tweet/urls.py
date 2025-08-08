from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.tweet_list,name='tweet_list'),
    path('create/', views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit,name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete,name='tweet_delete'),
    path('register/', views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
     path('search/', views.search_view, name='search'),
     path('tweet/<int:tweet_id>/like/', views.like_tweet, name='like_tweet'),
    path('tweet/<int:tweet_id>/comment/', views.add_comment, name='add_comment'),
    
    
    
]