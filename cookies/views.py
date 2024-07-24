from django.shortcuts import render

# Create your views here.
'''
            D J A N G O     C O O K I E S 
        --------------------------------------
=>  Max Size supported by many browser is 4096 bytes.  
        
=>  HttpRequest.COOKIES - A dict containig all cookies. Keys and Values both are strings.

=> set_cookie() - set_cookie() is used to set/create/sent cookies.
    

    @SYNTAX :-

    HttpRequest.set_cookie(
    key = "key",                     # required arg  
    value="value",                   # required arg   
    max_age = None,                  # expires after sepecified seconds     # default None : expires when browser session expires
    expires=None,                    # expirs at the sepcified datae        # format "Wdy, DD-Mon-YY HH:MM:SS GMT" or a datetime.datetime object in UTC.
    path='/,                         # deafult = '/' cookie will be sent for all the url on a specific website(domain matches)      # if set to "/app" than cookies willl only sent to tje request urls which will have /app just after the domain 
    domain=None,                     # domains that can read the cookie     # default None : only the exact domain that sets the cookie can read it.        # domain = "a.com" now domain with a.a.com, xy.a.xom, www.a.com can also read the cokkie.    
    secure=False,                    # if set to True than cookie can only be transmitted(set, receive) over secure connection only as https not http.   
    httponly=False,                  # by setting it true we can restrict the client-side javascript from having access to the cokkie.   
    samesite=None,                   # default 'Lax'    #samesite = 'Strict' or samesite = 'Lax' to tell the browser not to send this cookie when performing a cross-origin request.
    )

    e.g:- set_cookie("name", "cookie")
    e.g:- set_cookie("key", "value", max_age = 60*60*24*10)                                         expires after 10 days
    e.g:- set_cookie("key", "value", expires = datetime.utcnow() + timedelta(days=10))              expires after 10 days
    e.g:- set_cookie("key", "value", domain = "emart.com")                                          cookie is readable by domains like www.emart.com, xyz.emart.com, emart.com
    e.g:- set_cookie("key", "value", domain = "emart.com", path = '/')                              cookie will be sent to all the urls/endpoint/apis of the domain emart.com
    e.g:- set_cookie("key", "value", domain = "emart.com", path = '/app')                           cookie will be only be sent to  the urls/endpoint/apis of the domain emart.com which will have /app in request url.  "sent: www.emart.com/app/target", "not sent : www.emart.com/wow/app/target"
'''