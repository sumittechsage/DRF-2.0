


'''
            D J A N G O     C O O K I E S 
        --------------------------------------
=>  Max Size supported by many browser is 4096 bytes.  
        
=>  HttpRequest.COOKIES - A dict containig all cookies. Keys and Values both are strings.

'''

'''
                S E T   C O O K I E S
            ------------------------------
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
    samesite=None,                   # default 'Lax' in most browser    #samesite = 'Strict' - cookies will not be sent with any cross origin request    #samesite = 'Lax' - cookies will not be sent with cross-site requests except when the user navigates to the URL from an external site.         # None :- cookies will be sent with both cross-request and same site requests.

    e.g:- set_cookie("name", "cookie")
    e.g:- set_cookie("key", "value", max_age = 60*60*24*10)                                         expires after 10 days
    e.g:- set_cookie("key", "value", expires = datetime.utcnow() + timedelta(days=10))              expires after 10 days
    e.g:- set_cookie("key", "value", domain = "emart.com")                                          cookie is readable by domains like www.emart.com, xyz.emart.com, emart.com
    e.g:- set_cookie("key", "value", domain = "emart.com", path = '/')                              cookie will be sent to all the urls/endpoint/apis of the domain emart.com
    e.g:- set_cookie("key", "value", domain = "emart.com", path = '/app')                           cookie will be only be sent to  the urls/endpoint/apis of the domain emart.com which will have /app in request url.  "sent: www.emart.com/app/target", "not sent : www.emart.com/wow/app/target"
'''


'''
                R E A D  /  A C C E S S     C O O K I E S
            ----------------------------------------------------
        
        @SYNTAX :- request.COOKIES['key']

        e.g :-     name = request.COOKIES['name']

'''


'''
                R E P L A C E  /  A P P E N D     C O O K I E S
            --------------------------------------------------------
        CONCEPT :- when we assign  a new value to cookie, the current cookie are not replaced. The new cookie is parsed and its name-value pair is appended to the list. 
                   The exception is when you assing a new cookie with the same name (and same domain and path, if they exist) as cookie that already exists. In this case the old value is replaced with the new.
        

        e.g :-     set_cookie("name", "exam") will be replaced if set_cookie("name", "example")
        e.g :-     set_cookie("name", "exam") will be appended if set_cookie("last name", "example")

'''



'''
                D E L E T E     C O O K I E S
            --------------------------------------------------------
        CONCEPT :- The method is used to delete a  cookie with the same name (and same domain and path, if they exist), otherwise the cookie may not be deleted.
        

        @SYNTAX :- HttpResponse.delete_cookie(key, path='/', domain=None)

        e.g :-     delete_cookie("name") 
'''



