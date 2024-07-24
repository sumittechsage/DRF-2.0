from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
def setcookie(request):
    respone = Response({"message" : "cokkie set"}, status = 200)
    respone.set_cookie('name', 'santa')
    return 


def getcookie(request):
    cookies = request.COOKIES
    name = cookies['name']
    print("cookiees =====>", cookies)
    print("name from cookiee =====>", name)
    return Response({"message" : "cokkie read"}, status = 200)