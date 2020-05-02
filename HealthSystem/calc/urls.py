from django.urls import path
from rest_framework import routers #import Routers
from calc import views
from django.contrib import admin
from django.urls.conf import include
from django.views.generic.base import RedirectView
#routers use for create API of Machine Learning for connect ML model
router=routers.DefaultRouter() #decalare routers
router.register('diabetes',views.diabetesViewSet) #Register your routers
urlpatterns=[
    path('',views.home,name=''),
    path('home',views.home,name='home'),
    path('health',views.checkyourhealth, name='health'),
    path('contactus',views.contactus, name='contactus'),
    path('registration',views.registration, name='registration'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('checkdiabetes',views.checkdiabetes, name='checkdiabetes'),
    path('checkheart',views.checkheart, name='checkheart'),
    path('previoushealth',views.previoushealth, name='previoushealth'),

    path('graph',views.graph, name='graph'),

    
    path('api',include(router.urls)), #its for API Routers
    #path('model',views.create),
    #pat,views.logout, name='logout'),
    
    
    #path('check',views.check,name='check'),

]