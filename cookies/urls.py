from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setcookie, name = "set-cookie"),
    path('get/', views.getcookie, name = "get-cookie")
]
