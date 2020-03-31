from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework import viewsets
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from calc.serializers import diabetesSerializer
from calc.models import diabetes

# Create your views here.
def home (request):
    return render(request,'index.html')
def checkyourhealth(request):
    return render(request,'checkyourhealth.html')
def contactus(request):
    return render(request,'contactus.html')

def registration(request):
    if request.method== 'POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['psw']
        password2=request.POST['psw-repeat']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect("registration")
        
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email id taken')
                return redirect("registration")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save();
                messages.info(request,'Done')
                return redirect("login")
                
        else:
            messages.info(request,'Password not match')
            return redirect("registration")
        return redirect('/')

    else:
        return render(request,'registration.html')
def login(request):
    if request.method== 'POST':
         username=request.POST['username']
         password=request.POST['psw']
         user=auth.authenticate(username=username,password=password)
         

         if user is not None:
             auth.login(request,user)
             return redirect("/")
         else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
         return render(request,'login.html')
        


def logout(request):
    auth.logout(request)
    return redirect('/')

class diabetesViewSet(viewsets.ModelViewSet):
    queryset=diabetes.objects.all()
    serializer_class=diabetesSerializer
    #def create(self,request):
     #   if request.method=='GET':
        #senetence is the query we want to get the predicition for
       #     params=request.GET.get('sentence')
        #predict method used to get the prediction
        #    response=WebappConfig.predictor.predict(sentence)
        #return JSON responce
      #      return JsonResponse(response)
   # queryset=diabetes.objects.all()
    #serializer_class=diabetesSerializers