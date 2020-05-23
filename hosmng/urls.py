from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signin/',views.signin,name='signin'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    ##Patient's URL'S
    path('appointment/<str:id>',views.appointment,name='appointment'),
    path('Payment/<str:id>',views.Payment,name='Payment'),
    path('profile/<str:id>',views.Profile_page,name='Profile_page'),
    path('medical/<str:id>',views.medical,name='medical'),

    ##Doctors Urls
    path('Profile/<str:id>',views.profile,name='Profile'),
    path('patient/<str:id>',views.patient,name='patient'),
    path('prescribe/<str:id>',views.prescribe,name='prescribe'),
    path('prescribeform/<str:id>',views.prescribeform,name='prescribeform'),

    ## Reciption Urls
    path('dashboard/<str:id>',views.dashboard,name='dashboard'),
    path('pat_form/<str:id>',views.pat_form,name='pat_form'),
    path('update_pat/<str:id>',views.update_pat,name='update_pat'),
    path('delete_pat/<str:id>',views.delete_pat,name='delete_pat'),
    path('apt_form/<str:id>',views.apt_form,name='apt_form'),

    ## HR URL'S
    path('dashboard1/<str:id>',views.dashboard1,name='dashboard1'),
    path('update_doc/<str:id>',views.update_doc,name='update_doc'),
    path('delete_doc/<str:id>',views.delete_doc,name='delete_doc'),
    path('hospital_acc/<str:id>',views.hospital_acc,name='hospital_acc'),
    path('send/<str:id>',views.send,name='send'),
]