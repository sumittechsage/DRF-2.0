import logging
import time

# Function based middleware

def MiddlewareHook1(get_response):
    print("one time initialization")

    def middleware_function(request):
        print("This is before view")
        response = get_response(request)
        print("response =====>", response)
        print("This is after view")
        return response
    return middleware_function



# CLASS BASED MIDDLEWARE
logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        print("logger middleware")
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        print("logger middleware start time: ", start_time)
        response = self.get_response(request)
        duration = time.time() - start_time
        print("logger middleware duration: ", duration)
        logger.info(f'{request.method} {request.path} completed in {duration}s with status {response.status_code}')

        return response
    

# OLD STYLE HOOKS :-

from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class OldStyleCustomMiddleware(MiddlewareMixin):
    # H O O K S :::- 
    '''
    Django's middleware system allows middleware classes to define the following hooks:

    1. __init__: Called once when the web server starts.
    2. process_request: Called on each request before Django decides which view to execute.
    3. process_view: Called just before Django calls the view.
    4. process_exception: Called if the view raises an exception.
    5. process_response: Called on each request after the view is called.
    6. process_template_response: Called just after the view has finished executing, if the response contains a render method.
    '''

    def __init__(self, get_response):
        self.get_response = get_response
        print("OLD STYLE HOOKS INITALISATION")
        # One-time configuration and initialization.

    def process_request(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Processing request in old style middleware")
        # Example: Add a custom header to the request
        request.META['CUSTOM_HEADER'] = 'CustomValue'

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Code to be executed just before the view is called.
        print("Processing view in old style middleware")
        # Example: Log the view being called
        print(f"View: {view_func.__name__}")

    def process_exception(self, request, exception):
        # Code to be executed if an exception is raised.
        print("Processing exception in old style middleware")
        # Example: Log the exception
        print(f"Exception: {exception}")
        # Return None to continue processing the exception, or a response to handle it
        return None

    def process_response(self, request, response):
        # Code to be executed for each request/response after
        # the view is called.
        print("Processing response in old style middleware")
        # Example: Add a custom header to the response
        response['CUSTOM_HEADER'] = 'CustomValue'
        return response

    def process_template_response(self, request, response):
        # Code to be executed if the response contains a `render` method
        print("Processing template response in old style middleware")
        # Example: Modify the context of the template response
        response.context_data['custom_context'] = 'CustomValue'
        return response




# NEW STYLE HOOKS

class NewStyleCustomMiddleware:
    """
    Django's middleware system allows middleware classes to define the following hooks:

    1. __init__: Called once when the web server starts.
    2. process_request: Called on each request before Django decides which view to execute.
    3. process_view: Called just before Django calls the view.
    4. process_exception: Called if the view raises an exception.
    5. process_response: Called on each request after the view is called.
    6. process_template_response: Called just after the view has finished executing, if the response contains a render method.
    """
    
    def __init__(self, get_response):
        """
        One-time configuration and initialization.
        """
        self.get_response = get_response
        print("NEW STYLE Middleware initialized")

    def __call__(self, request):
        """
        Handle request and response processing.
        """
        # Code to be executed for each request before the view is called.
        self.process_request(request)
        
        # Get the response from the next middleware or view.
        response = self.get_response(request)
        
        # Handle template responses.
        if hasattr(response, 'render') and callable(response.render):
            response = self.process_template_response(request, response)
        
        # Code to be executed for each request/response after the view is called.
        response = self.process_response(request, response)
        
        return response
    
    def process_request(self, request):
        """
        Code to be executed for each request before the view (and later middleware) are called.
        """
        print("Processing request in new style middleware")
        # Example: Add a custom header to the request
        request.META['CUSTOM_HEADER'] = 'CustomValue'
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Code to be executed just before the view is called.
        """
        print("Processing view in new style middleware")
        # Example: Log the view being called
        print(f"View: {view_func.__name__}")
        return None  # Returning None allows the request to continue

    def process_exception(self, request, exception):
        """
        Code to be executed if an exception is raised.
        """
        print("Processing exception in new style middleware")
        # Example: Log the exception
        print(f"Exception: {exception}")
        return JsonResponse({'exception' : 'exception'}, status = 500)  # Returning None continues processing the exception
    
    def process_response(self, request, response):
        """
        Code to be executed for each request/response after the view is called.
        """
        print("Processing response in new style middleware")
        # Example: Add a custom header to the response
        response['CUSTOM_HEADER'] = 'CustomValue'
        return response
    
    def process_template_response(self, request, response):
        """
        Code to be executed if the response contains a `render` method.
        """
        print("Processing template response in new style middleware")
        # Example: Modify the context of the template response
        response.context_data['custom_context'] = 'CustomValue'
        return response
