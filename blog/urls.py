from django.contrib import admin
from django.urls import path
from blog.views import *
app_name='blog'

urlpatterns = [
    path('',blog_view,name='blog'),
    path('single-blog/',single_view,name='single')
]
