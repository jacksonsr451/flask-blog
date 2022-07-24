from functools import wraps
from flask import request, Response



def csrf_token_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        
        role = request.data
        
        if role["csrf_token"] == "123456":
            return func(*args, **kwargs)
        
        return Response('Authorization failed', mimetype='text/plain', status=404)
        
    
    return decorated_function
