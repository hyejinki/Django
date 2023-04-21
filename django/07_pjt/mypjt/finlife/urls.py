from django.urls import path
from finlife import views

urlpatterns = [
    # path('api_test/', views.api_test),
    path('save_deposit_products/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_product_options),
]
