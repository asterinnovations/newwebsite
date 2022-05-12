from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contacts'),
    path('team/',views.team,name='team'),
    path('terms/',views.terms,name='terms'),
    path('cliq/',views.cliq,name='cliq'),

    path('privacy/',views.privacy,name='privacy'),
    path('otp/',views.otp,name='otp'),
    path('omis/',views.omis,name='omis')

]
