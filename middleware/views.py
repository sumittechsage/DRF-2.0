from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import random

def testing_function_based_middleware(request):
    print("This is function-based view")
    return JsonResponse({"message": "learning middleware"}, status = 200)


def logger_middleware(request):
    print("LOGGER MIDDLEWARE TESTING VIEW")
    return JsonResponse({"message": "logger middleware"}, status = 200)

def exception_middleware(request):
    print("EXCEPTION MIDDLEWARE TESTING VIEW")
    if random.randint(1,6)%2 :
        raise Exception("EXCEPTION MIDDLEWARE")
    return JsonResponse({"message": "exception middleware"}, status = 200)