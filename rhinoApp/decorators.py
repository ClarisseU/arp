from django.http import HttpResponse
from django.shortcuts import redirect

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        elif request.user.is_authenticated == None:
            return redirect('login')
        else:    
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all[0].name

                if group in allowed_roles: 
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("You are not allowed to view this page")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all[0].name

        if group == 'hw':
            return redirect('user-page')

        if group == 'parent':
            return view_func(request, *args, **kwargs)
        else: 
            return HttpResponse("You are not allowed to view this page")

    return wrapper_func
