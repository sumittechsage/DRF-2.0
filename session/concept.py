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

'''
                                S E S S I O N   M E T H O D S 
                            - - - - - - - - - - - - - - - - - - - 
                        
                        !!! By default session expiry is of 2 weeks !!!

=> get_session_cookie_age() - It returns the age of session cookies, in seconds. Defaults to SESSION_COOKIE_AGE.

=> set_expiry(value) -  ! It sets the expiration time for the session. You can  pass a number of different values.
                        ! If values is an integer, the session will expire after that many seconds of inactivity. 
                            e.g:- calling request.session.set_expiry(300) would make the session expire in 5minutes.
                        ! If value is datetime or timedelta object, the session will expire at the specific data/time. Note that datetime and timedelta values are only serializable if you are using the PickleSerializer.
                        ! If value is 0, user's session cookie will expire when the user's web browser is closed.
                        ! If the value is NOne session reverts to using the global session expiry policy.
                        ! Reading a session is not considered activity for expiration purposes. Session expiration is computed from the last time the session was modified.

=> get_expiry_age() - ! It returns the number of seconds until this session expires. 
                      ! For sessions with no custom expiration (or those set to expire at browser close), this will equal SESSION_COOKIE_AGE
                      ! This function accepts two optinal keyword args:
                            a) modification : last modificcation of the session, as a datetime object, an int(in seconds), or None. Defaults to the current time.
                            a) expiry : expiry information for the session, a s a datetime object, an int(in seconds), or None. Defaults to the vlaue stored in the session by set_expiry(), if there is one, or None.

=> get_expiry_date() -  ! It returns the date this session will expire. For sessions with no custom expiration(or those set to expire at browser close), this will equal the date SESSION_COOKIE_AGE seconds from now.
                        ! This function accepts the same keyword arguments as get_expiry_age().

=> clear_expired() - ! It removes expired sessions from the session store. 
                     ! This class methods is called by clearsessions.

=> set_test_cookie() - ! It sets a test cookie to determine whether the user's browser supports cookies.
                       ! Due to the way cokkies work, you won't be able to test this until the user's next page request.

=> test_cookie_worked() - ! It returns either True or False, depending on whether the user's browser accepted the test cookie.                       
                          ! Due to the way cokkies work, you will have to call set_test_cookie() on a previous, seperate page request.

=> delete_test_cookie() - ! It deletes the test cookie. Use this to cleanup after verifying.           
'''