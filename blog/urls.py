from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'blog.views.home', name='home'),

]










