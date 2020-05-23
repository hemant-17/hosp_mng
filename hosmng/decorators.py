from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,id,*args,**kwargs):
            group = None
            #print(request.user.group)
            query_set = Group.objects.filter(user = request.user)
            for g in query_set:
                print(g.name)
                group = g.name
            # if request.user.group.exists():
            #     group= request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,id,*args,**kwargs)

            else:
                return HttpResponse('You are not Authorized to view this')
        return wrapper_func

    return decorator