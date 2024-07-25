from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setsession, name = "set-session"),
    path('get/', views.getsession, name = "get-session"),
    path('delete/', views.deletesession, name = "delete-session"),
    path('setdefault/', views.setdefualtsession, name = "setdeafult-session"),
    path('flush/', views.flushsession, name = "flush-session"),
    path('set-expires/', views.setsessionexpireage, name = "set-expires-session"),
    path('expires/', views.checksessionage, name = "expires-session"),
    path('set-test/', views.settestcookie, name = "set-test-cookies"),
    path('check-test/', views.checktestcookie, name = "check-test-cookies"),
    path('delete-test/', views.deletetestcookie, name = "delete-test-cokkies"),
]
