from django.core.exceptions import PermissionDenied

def user_is_seller(func):
    
    def wrapper(request, *args, **kwargs):
        if not request.user.is_customer:
            return func(request, *args, **kwargs)
        else:
            return PermissionDenied

    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper