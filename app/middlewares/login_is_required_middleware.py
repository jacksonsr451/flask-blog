from functools import wraps
from flask import flash, redirect, request, Response
from flask_login import current_user


def login_is_required_middleware(func):
    
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return func(*args, **kwargs)
        
        flash("Login is required!", "error")
        return redirect('/auth/login')
    
    return decorated_function
