from django.urls import path
from . import views

app_name = 'calculation'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('calculation/', views.throw, name='throw'),
    path('result/', views.catch, name='catch'),
]
