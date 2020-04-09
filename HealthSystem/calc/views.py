from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework import viewsets
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from calc.serializers import diabetesSerializer
from calc.models import diabetes
from calc import diabetesmodel
import pandas as pd

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

class diabetesViewSet(viewsets.ModelViewSet): #Its Code for API now here Create API of Machine Learning
            queryset=diabetes.objects.all() #take all objects mean all field 
            serializer_class=diabetesSerializer

    

    #def create(self,request,*args,**kwargs):#override Create method of ViewSet
     #   ob= diabetes.objects.latest("id")#its for fetch lastest record from diabetes table database
      #  print(type(ob))
       # yes=diabetesmodel.prediction(ob)#its pass data of lastest rows to the model for prediction
     #   if request.method=='GET':
        #senetence is the query we want to get the predicition for
       #     params=request.GET.get('sentence')
        #predict method used to get the prediction
        #    response=WebappConfig.predictor.predict(sentence)
        #return JSON responce
      #      return JsonResponse(response)
   # queryset=diabetes.objects.all()
    #serializer_class=diabetesSerializers
def checkdiabetes(request):
    if request.method== 'POST':

        Pregnancies=request.POST['Pregnancies']
        Glucose=request.POST['Glucose']
        BloodPressure=request.POST['BloodPressure']
        SkinThickness=request.POST['SkinThickness']
        Insulin=request.POST['Insulin']
        BMI=request.POST['BMI']
        DiabetesPedigreeFunction=request.POST['DiabetesPedigreeFunction']
        Age=request.POST['Age']
        #convert into integer
        Pregnancies=int(Pregnancies)
        Glucose=int(Glucose)
        BloodPressure=int(BloodPressure)
        SkinThickness=int(SkinThickness)
        Insulin=int(Insulin)
        BMI=float(BMI)
        DiabetesPedigreeFunction=float(DiabetesPedigreeFunction)
        Age=int(Age)




        x = [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]#problem is here
        

        #myDict=(request.POST).dict()
        df=pd.DataFrame(x,index=[0])
        pre=diabetesmodel.prediction(df)
        dia=diabetes.objects.create(Pregnancies=Pregnancies,Glucose=Glucose,BloodPressure=BloodPressure,SkinThickness=SkinThickness,Insulin=Insulin,BMI=BMI,DiabetesPedigreeFunction=DiabetesPedigreeFunction,Age=Age,Outcome=pre)
        dia.save();


        for i in pre:
            if i==0:
                return render(request,'result1.html')

                
            else:
               return render(request,'result.html')

        return redirect("checkdiabetes")
        #print(df)
        #print(type(df))
        #return redirect('/')
    else:
        return render(request,'diabetes.html')

def check (request):
    return render(request,'result.html')