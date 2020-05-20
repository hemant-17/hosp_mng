from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        query_set = Group.objects.filter(user = request.user)
        for g in query_set:
            group = g.name
        return render(request,"index.html",{'context':group})
    else:
        return render(request,'index.html')

def about(request):
    return HttpResponse("This is our about page")

def contact(request):
    return HttpResponse("This is our contact page")


@unauthenticated_user
def signin(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already registered')
                return redirect('signin')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already registered")
                return redirect('signin')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Confirm Password did not mathch")
            return redirect('signin')




    return render(request,"signup.html")


@unauthenticated_user
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        User=auth.authenticate(username=username,password=password)

        if User is not None:
            auth.login(request ,User)
            return redirect('/')
        else:
             messages.info(request,'Invalid Credentials')
             return redirect('login')


    return render(request,"login.html")


@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/')

### Patients Views
@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Patient'])
def appointment(request):

    # this should print all group names for the user

    return HttpResponse("APPOINTMENT")

@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Patient'])
def Payment(request):
    return HttpResponse("Payment")


### Doctors Views
@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Doctor'])
def profile(request):
    return HttpResponse("Profile")

@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Doctor'])
def patient(request):
    return HttpResponse("Patient")