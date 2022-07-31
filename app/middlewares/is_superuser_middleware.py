from functools import wraps
from flask import flash, redirect, request, Response
from flask_login import current_user


def is_superuser_middleware(func):
    
    @wraps(func)
    def decorated_function(*args, **kwargs):
        for current_role in current_user.roles():
            if current_role['role'] == "superuser":
                return func(*args, **kwargs)
        
        flash("Superuser is required by access this route!", "error")
        return redirect('/auth/login')
    
    return decorated_function
