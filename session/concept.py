'''
                            S E S S I O N       F R A M E W O R K 
                        - - - - - - - - - - - - - - - - - - - - - - - 

=> The session framework lets you store and retrieve arbitrary data on a per-site-visitor basis.
=> It stores data on the server side and abstracts the sending and receiving of cookies, 
=> In session : Cookies contain a session ID not the data itself.

=> By default Django stores session in your db
=> As it stores sessoins in the database so it is mandatory to run makemigrations and migrate to use session.
=> IT will create required tables.

=> The Django sessions framework is entirely, and solely, cookie-based.

=> SETTINGS.PY  
        middleware :-       django.contrib.sessions.middleware.SessionMiddleware
        installed_apps :-   django.contrib.sessions

'''

###########################################################################################################################################################################

'''
                                T Y P E S    O F     S E S S I O N S
                            - - - - - - - - - - - - - - - - - - - - - - -

#1.  DATABASE BACKED SESSIONS 
            -- If you want to use this session, you need to add 'django.contrib.sessions' to installed_apps. 
            -- Then make makemigrations.

#2.  FILE BASED SESSIONS 
            -- To use file-based-sessions, set the SESSION_ENGINE setting to "django.contrib.sessions.backends.file".
            -- Additionally, you might want to set the SESSION_FILE_PATH setting (which defaults to output from tempfile.gettempdir(), most likely /temp) to control  where Django stores session files. Be sure to check that your web server has permissions to read and write this location.

#3.  COOKIE BASED SESSIONS
            -- To use cookie based sessions, set the SESSION_ENGINE settings to "django.contrib.sessions.backends.signed_cookies".
            -- The session data will be stored using Django's tools for cryptographiv signing and the SECRET_KEY settings.

#4.  CACHE SESSIONS
            -- For better performanace, you may want to use a cache-based session backends. To store sesion data using Django's cache system, you'll first need to make sure you've configured your cache.            
'''


###########################################################################################################################################################################

'''
                                U S I N G   S E S S I O N S    I N  V I E W S 
                            - - - - - - - - - - - - - - - - - - - - - - - - - - -

=> When SessionMiddleware is activated, each HttpRequest object, the first argument to any Django view function will have a session attribute, which is a dictionary-like object
=> You can read it and write to request.session at any point in your view. You can edit it multiple times.


@SET ITEM IN THE SESSION :-
    request.session['key'] = 'item'


@GET ITEM FROM SESSION :-
    item = request.session['key']

    
@DELETE ITEM FROM SESSION :-
    del request.session['key]
    !! if 'key' does'nt exists then keyerror will be raised.

    
@TO CHECK IF A KEY IS IN SESSION OR NOT:-
    if 'key' in request.session
'''

###########################################################################################################################################################################