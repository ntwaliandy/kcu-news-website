from os import name
from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]