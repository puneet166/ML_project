from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request,'index.html')
def checkyourhealth(request):
    return render(request,'checkyourhealth.html')
def registration(request):
    return render(request,'registration.html')
def contactus(request):
    return render(request,'contactus.html')
def login(request):
    return render(request,'login.html')