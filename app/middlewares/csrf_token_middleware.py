from functools import wraps
from flask import request, Response

from app.ext.flask_wtf import csrf



def csrf_token_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        
        role = request.data
        
        if csrf.validate_csrf(role["csrf_token"]):
            return func(*args, **kwargs)
        
        return Response('Authorization failed', mimetype='text/plain', status=404)
        
    
    return decorated_function
