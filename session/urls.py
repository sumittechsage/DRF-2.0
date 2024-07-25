from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setsession, name = "set-session"),
    path('setdefault/', views.setdefualtsession, name = "setdeafult-session"),
    path('get/', views.getsession, name = "get-session"),
    path('delete/', views.deletesession, name = "delete-session"),
    path('flush/', views.flushsession, name = "flush-session"),
]
