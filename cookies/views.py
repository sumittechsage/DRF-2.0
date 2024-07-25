from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
def setcookie(request):
    respone = JsonResponse({"message" : "cokkie set"}, status = 200)
    respone.set_cookie('name', 'banta', httponly=False)
    return  respone


def getcookie(request):
    cookies = request.COOKIES
    name = cookies['name']
    print("cookiees =====>", cookies)
    print("name from cookiee =====>", name)
    return JsonResponse({"message" : "cokkie read"}, status = 200)

def deletecookie(request):
    cookies = request.COOKIES
    name = cookies['name']
    print("cookiees =====>", cookies)
    print("name from cookiee =====>", name)

    response = JsonResponse({"message" : "cokkie deleted"}, status = 200)
    response.delete_cookie('name')
    return response


# SIGNED COOKIE :- 
'''
    we have to provide a salt to sign the cookie so if the cookie is edited by the client it will change the signatere(hash) and we will know the value is edited.
'''
def setsignedcookie(request):
    respone = JsonResponse({"message" : "cokkie set"}, status = 200)
    # salt = 'signature
    respone.set_signed_cookie('name', 'prof', salt = 'signature', httponly=False)
    return  respone


def getsignedcookie(request):
    # salt = 'signature  # provided when setting the cookie
    name = request.get_signed_cookie('name', salt = 'signature')
    print("name =====>", name)
    return JsonResponse({"message" : "cokkie read"}, status = 200)