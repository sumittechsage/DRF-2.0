from django.urls import path
from . import views

urlpatterns = [
    path('function-1/', views.testing_function_based_middleware, name='function'),
    path('logger/', views.logger_middleware, name='logger'),
    path('exception/', views.exception_middleware, name='exception'),
]
