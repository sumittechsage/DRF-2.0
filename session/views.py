from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
def setsession(request):
    request.session['name'] = 'Session_name'
    return JsonResponse({"message" : "session set"}, status = 200)


def setdefualtsession(request):
    ''' DICTIONARY METHOD "setdefault(key, value)" : if a key exsists return its value other wise insert key with value given.'''
    age = request.session.setdefault('age', '26')
    print("age ====>", age)
    return JsonResponse({"message" : "session default set"}, status = 200)


def getsession(request):
    session= request.session
    name = session['name']
    print("session =====>", session)
    print("name from session =====>", name)
    return JsonResponse({"message" : "session read"}, status = 200)

def deletesession(request):
    ''' DELETES DATA FROM SESSION NOT THE SESSION ITSELF'''
    session = request.session
    name = session['name']
    print("cookiees =====>", session)
    print("name from cookiee =====>", name)
    del session['name']
    return JsonResponse({"message" : "session deleted"}, status = 200)
  

def flushsession(request):
    ''' DELETE THE DATA AND COOKIES/SESSION : E.G :- LOGOUT FUNCTION'''
    session = request.session
    session.flush()
    return JsonResponse({"message" : "session flushed"}, status = 200)
