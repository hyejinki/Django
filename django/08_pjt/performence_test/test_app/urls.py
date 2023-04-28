from django.urls import path
from . import views

urlpatterns = [
    path('pandas_read/', views.pandas_read),
    path('similar_age/', views.similar_age),
   
]

