from django.urls import path

from . import views
urlpatterns=[
    path('',views.home,name=''),
    path('',views.home,name='home'),
    path('health',views.checkyourhealth, name='checkyourhealth'),
    path('registration',views.registration, name='Reg'),
    path('contactus',views.contactus, name='contactus'),
    path('logingo',views.login, name='login'),
    

]