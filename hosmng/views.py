from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from . models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        group=get_group(request)
        # query_set = Group.objects.filter(user = request.user)
        # for g in query_set:
        #     group = g.name
        return render(request,"index.html",{'context':group})
    else:
        return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    sent = request.user.email
    recipient_list = ['sent']
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/')

def get_group(request):
        query_set = Group.objects.filter(user = request.user)
        for g in query_set:
            group = g.name
        #print(group)
        return group


@unauthenticated_user
def signin(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')
        gr = request.POST.get('choice','')

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
                if gr == 'Doctor':
                    my_group = Group.objects.get(name='Doctor')
                    user.groups.add(my_group)
                else:
                    my_group = Group.objects.get(name='Patient')
                    user.groups.add(my_group)


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
def appointment(request,id):
    group=get_group(request)
    query_set = Appointment.objects.filter(pat_name = request.user).order_by('-date')
    return render(request,"appointment.html",{'context':group,"object_list":query_set})


@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Patient'])
def Payment(request,id):
    group=get_group(request)
    query_set = Medical.objects.filter(patname = request.user).order_by('-date')
    return render(request,"invoice.html",{'context':group,"object_list":query_set})


@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Patient'])
def Profile_page(request,id):
    group=get_group(request)
    patient = request.user.patient
    form = ProfileForm(instance=patient)
    if request.method == 'POST':
        #print(form['register'].value())
        form = ProfileForm(request.POST, request.FILES,instance=patient)
        if form.is_valid():
            form.save()

    return render(request,'profile.html',{'form':form,'context':group})

@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Patient'])
def medical(request,id):
    group=get_group(request)
    query_set = Medical.objects.filter(patname = request.user).order_by('-date')
    files = Patient.objects.filter(user=request.user).values('med_reps')
    return render(request,"medical.html",{'context':group,"object_list":query_set,'file':files})



### Doctors Views
@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Doctor'])
def profile(request,id):
    group=get_group(request)
    form = DocForm()
    if request.method == 'POST':
        form = DocForm(request.POST)
        if form.is_valid():
            st = form.save(commit=False)
            st.user = request.user
            st.save()
            return redirect('/')
    return render(request,'doc_profile.html',{'context':group,'form':form})

@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Doctor'])
def patient(request,id):
    group=get_group(request)
    query_set = Appointment.objects.filter(doc_name = request.user).order_by('-date')
    return render(request,"available.html",{'context':group,"object_list":query_set})




@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Doctor'])
def prescribe(request,id):
    group=get_group(request)
   # print(localdate())
    query_set = Medical.objects.filter(docname = request.user).order_by('-date')
    return render(request,"prescribe.html",{'context':group,"object_list":query_set})

@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Doctor'])
def prescribeform(request,id):
    group=get_group(request)
    query_set = Medical.objects.filter(docname = request.user).order_by('-date')
    if request.method == 'POST':
        form = MedicalForm(request.POST)
        if form.is_valid():
            st = form.save(commit=False)
            st.date = localdate()
            st.docname = request.user
            st.save()
        return render(request,"prescribeform.html",{'context':group,"form":form})
    else:
        form = MedicalForm(request.POST)
        return render(request,"prescribeform.html",{'context':group,"form":form})

## Reception Views
@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Receptionist'])
def dashboard(request , id):
    group=get_group(request)
    app = Appointment.objects.all().count()

    comp = Appointment.objects.filter(status='Completed').count()

    pend = Appointment.objects.filter(status='Pending').count()
    query_set = Appointment.objects.all().order_by('-date')
    query_set1 = Patient.objects.all().order_by('date')
    return render(request,'dashboard.html',{'context':group,'app':app,'comp':comp,'pend':pend,"object_list":query_set,'obj_list':query_set1})

@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Receptionist'])
def pat_form(request,id):
    group=get_group(request)
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    return render(request,'pat_form.html',{'context':group,'form':form})

@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Receptionist'])
def update_pat(request,id):
    group=get_group(request)
    pat = Patient.objects.get(id=id)
    form = PatientForm(instance=pat)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance = pat)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'pat_form.html',{'context':group,'form':form})



@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Receptionist'])
def delete_pat(request,id):
    # print(pk)
    order = Patient.objects.get(id=id)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'delete.html', context)


@login_required(login_url='/login')
@allowed_users(allowed_roles = ['Receptionist'])
def apt_form(request,id):
    group=get_group(request)
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,"apt_form.html",{'context':group,'form':form})

## HR Views
@login_required(login_url='/login')
@allowed_users(allowed_roles = ['HR'])
def dashboard1(request,id):
    group=get_group(request)
    app = Doctor.objects.all().count()

    comp = Patient.objects.all().count()

    pend = Doctor.objects.filter(status='Active').count()
    query_set = Doctor.objects.all()
    return render(request,"hr_dash.html",{'context':group,'app':app,'comp':comp,'pend':pend,"object_list":query_set})

@login_required(login_url='/login')
@allowed_users(allowed_roles = ['HR'])
def update_doc(request,id):
    group=get_group(request)
    pat = Doctor.objects.get(id=id)
    form = DoctorForm(instance=pat)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance = pat)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'doc_form.html',{'context':group,'form':form})



@login_required(login_url='/login')
@allowed_users(allowed_roles = ['HR'])
def delete_doc(request,id):
    # print(pk)
    order = Doctor.objects.get(id=id)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'delete.html', context)

@login_required(login_url='/login')
@allowed_users(allowed_roles = ['HR'])
def hospital_acc(request,id):
    group=get_group(request)
    med = Medical.objects.all()
    pat = Patient.objects.all()
    count = Patient.objects.all().count()
    print(count)
    return render(request,"hos_acc.html",{'context':group,'med':med,'obj':pat})

@login_required(login_url='/login')
@allowed_users(allowed_roles = ['HR'])
def send(request,id):
    info = Patient.objects.filter(id=id).values('email','outstanding')
    print(info[0]['email'],info[0]['outstanding'])
    email_add = info[0]['email']
    print(email_add)
    subject = 'Regarding outstanding at Docmed hospital'
    message = ' Please pay your outstanding of ' + str(info[0]['outstanding']) + 'as early as possible , so that we can continue our services for you seemlessly'
    email_from = settings.EMAIL_HOST_USER
    sent = request.user.email
    recipient_list = [email_add]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse("Message send")