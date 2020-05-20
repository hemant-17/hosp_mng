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

    ##Doctors Urls
    path('Profile/<str:id>',views.profile,name='Profile'),
    path('patient/<str:id>',views.patient,name='patient'),

]