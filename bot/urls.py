from django.contrib import admin
from django.urls import path,include
from .views import getPostsView,getPostLikersView

urlpatterns = [
    path('get_posts/',  getPostsView),
    path('get_likers/',  getPostLikersView),
]
