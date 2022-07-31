from functools import wraps
from flask import flash, request, Response
from flask_login import current_user


def is_superuser_middleware(func):
    
    @wraps(func)
    def decorated_function(*args, **kwargs):
        for current_role in current_user.roles():
            if current_role['role'] == "superuser":
                return func(*args, **kwargs)
            
        return Response('Authorization failed', mimetype='text/plain', status=404)
    
    return decorated_function
