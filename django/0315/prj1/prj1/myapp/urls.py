from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:number>/', views.detail, name = 'detail'),
    path('calc/<int:number1>/<int:number2>', views.calc),
    path('price/<str:thing>/<int:price>', views.price),
    
    
]