
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('articles/', views.articles, name='articles'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
    path('new/', views.new, name='new'),
    path('remv/', views.remv, name='remv'),

]
