from django.urls import path
from rest_framework import routers
from calc import views
from django.contrib import admin
from django.urls.conf import include
#from api import views
router=routers.DefaultRouter()
router.register('model',views.diabetesViewSet)
urlpatterns=[
    path('',views.home,name=''),
    path('home',views.home,name='home'),
    path('health',views.checkyourhealth, name='health'),
    path('contactus',views.contactus, name='contactus'),
    path('registration',views.registration, name='registration'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('model',include(router.urls)),
    #pat,views.logout, name='logout'),
    
    
    

]