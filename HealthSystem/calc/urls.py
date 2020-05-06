from django.urls import path
from rest_framework import routers #import Routers
from calc import views
from django.contrib import admin
from django.contrib.auth import views as auth_views 
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
    path('comparehealth',views.comparehealth, name='comparehealth'),
    path('diet',views.diet, name='diet'),

    path('graph',views.graph, name='graph'),
    # all for reset password
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path("password_reset_complete",auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    # its all change password
    path('password_change',auth_views.PasswordChangeView.as_view(template_name='password_change.html'),name='password_change'),
    path('password_change_done',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),


    #its all heart graphs
    path('previousheart',views.previousheart, name='previousheart'),
    path('compareheart',views.compareheart, name='compareheart'),
    path('graphheart',views.graphheart, name='graphheart'),
    
   
    path('api',include(router.urls)), #its for API Routers
    #path('model',views.create),
    #pat,views.logout, name='logout'),
    
    
    #path('check',views.check,name='check'),

]