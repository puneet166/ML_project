from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework import viewsets
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from calc.serializers import diabetesSerializer
from calc.models import diabetes,heart,query,role,role_heart
from calc import diabetesmodel
import pandas as pd
from calc import models_heart
context={'pi':4}
context_heart={'pp':8}

# Create your views here.
def home (request):
    return render(request,'index.html')
def checkyourhealth(request):
    return render(request,'checkyourhealth.html')
def diet(request):
    return render(request,'diet.html') 



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
    if  request.user.is_authenticated:


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
            global context


            

            
            


            x = [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]#problem is here
        

            #myDict=(request.POST).dict()
            df=pd.DataFrame(x,index=[0])
            pre=diabetesmodel.prediction(df)
            dia=diabetes.objects.create(Pregnancies=Pregnancies,Glucose=Glucose,BloodPressure=BloodPressure,SkinThickness=SkinThickness,Insulin=Insulin,BMI=BMI,DiabetesPedigreeFunction=DiabetesPedigreeFunction,Age=Age,Outcome=pre)
            dia.save();


            info = diabetes.objects.latest('sno')
            info=info.sno
                        

            
            current_user = request.user
            current=current_user.id
            

            curr=User.objects.get(id=current)
            curr=curr.id
            
            dia1=role.objects.create(role_dia=info,User_mail=curr)
            dia1.save();


            Pregnancies=round((Pregnancies*100)/17)
            Glucose=round((Glucose*100)/200)
            BloodPressure=round((BloodPressure*100)/150)
            SkinThickness=round((SkinThickness*100)/100)
            Insulin=round((Insulin*100)/1000)
            

            




            context={'Pregnancies':Pregnancies,'Glucose':Glucose,'BloodPressure':BloodPressure,'SkinThickness':SkinThickness,
            'Insulin':Insulin,'BMI':BMI,'DiabetesPedigreeFunction':DiabetesPedigreeFunction,'Age':Age}
            print(context)

            for i in pre:
                if i==0:
                    return render(request,'diabetes_output.html')

                
                else:
                    return render(request,'diabetes_output1.html')

            return redirect("checkdiabetes")
        #print(df)
        #print(type(df))
        #return redirect('/')
        else:
            return render(request,'diabetes.html')
    else:
         return redirect('login')



def checkheart(request):
    if  request.user.is_authenticated:

            if request.method== 'POST':
                age=request.POST['age']
                sex=request.POST['drop1']
                cp=request.POST['drop2']
                trestbps=request.POST['trestbps']
                chol=request.POST['chol']
                fbs=request.POST['fbs']
                restecg=request.POST['drop3']
                thalach=request.POST['thalach']
                exang=request.POST['drop4']
                oldpeak=request.POST['oldpeak']
                slope=request.POST['drop5']
                ca=request.POST['drop6']
                thal=request.POST['drop7']


                age=int(age)
                sex=int(sex)
                cp=int(cp)
                trestbps=int(trestbps)
                chol=int(chol)
                fbs=int(fbs)
                if fbs >120:
                    fbs=1
                else:
                    fbs=0
                restecg=int(restecg)
                thalach=int(thalach)
                exang=int(exang)
                oldpeak=float(oldpeak)
                slope=int(slope)
                ca=int(ca)
                thal=int(thal)
                global context_heart





                x = [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
                df=pd.DataFrame(x,index=[0])
                pre=models_heart.prediction(df)
                dia=heart.objects.create(age=age,sex=sex,cp=cp,trestbps=trestbps,chol=chol,fbs=fbs,restecg=restecg,thalach=thalach,exang=exang,oldpeak=oldpeak,slope=slope,ca=ca,thal=thal,target=pre)
                dia.save();

                info = heart.objects.latest('sno_heart')

                info=info.sno_heart

                current_user = request.user
                current=current_user.id
            

                curr=User.objects.get(id=current)
                curr=curr.id

                dia1=role_heart.objects.create(role_heart=info,User_id=curr)
                dia1.save();
                # correct 

                trestbps=round((trestbps*100)/200)
                chol=round((chol*100)/700)
                fbs=round((fbs*100)/300)
                thalach=round((thalach*100)/250)
                context_heart={'age':age,'sex':sex,'cp':cp,
                    'trestbps':trestbps,'chol':chol,'fbs':fbs,'restecg':restecg ,'thalach':thalach,
                    'exang':exang,'oldpeak':oldpeak,'slope':slope,'ca':ca,'thal':thal}
                
            



                for i in pre:
                    if i==0:
                        return render(request,'heart_output1.html')

                
                    else:
                        return render(request,'heart_output2.html')

                return redirect("checkheart")
        #print(df)
        #print(type(df))
        #return redirect('/')
        
            
            
            else:
                return render(request,'heart.html')
    else:
        return redirect('login')


def contactus (request):
    if request.method== 'POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Message=request.POST['Message']
        query_mess=query.objects.create(Name=Name,Email=Email,Message=Message)
        query_mess.save();
        messages.info(request,'Query Submitted Sucessfully our Partner will contact soon on email')
        return redirect("contactus")
    else:
        return render(request,'contactus.html')




        #here all methods about diabetes graphs

        
def previoushealth(request):
    if  request.user.is_authenticated:

        listt=[]
        
        current_user = request.user
        current=current_user.id
        #print(type(current))
        curr=User.objects.get(id=current)
        #print(type(curr))
        curr=curr.id
        #print(type(curr))
        values = role.objects.filter(User_mail=curr)#its convert into list
    
    
        for value in values.all():
            pp=value.role_dia
            listt.append(pp)
    
        values = diabetes.objects.get(sno=listt[len(listt)-2])#its convert into list
        Pregnancies=round((values.Pregnancies*100)/17)
        Glucose=round((values.Glucose*100)/200)
        BloodPressure=round((values.BloodPressure*100)/150)
        SkinThickness=round((values.SkinThickness*100)/100)
        Insulin=round((values.Insulin*100)/1000)
        context={'Pregnancies':Pregnancies,'Glucose':Glucose,'BloodPressure':BloodPressure,'SkinThickness':SkinThickness,
            'Insulin':Insulin,'BMI':values.BMI,'DiabetesPedigreeFunction':values.DiabetesPedigreeFunction,'Age':values.Age}
               
        return render(request,'diabetesgraph.html',context)
        #print(values.BMI)
    else:
                return redirect('login')



def comparehealth(request):
    if  request.user.is_authenticated:

        listt=[]
          
        current_user = request.user
        current=current_user.id
        #print(type(current))
        curr=User.objects.get(id=current)
        #print(type(curr))
        curr=curr.id
        #print(type(curr))
        values = role.objects.filter(User_mail=curr)#its convert into list
    
    
        for value in values.all():
            pp=value.role_dia
            listt.append(pp)
    
        values = diabetes.objects.get(sno=listt[len(listt)-2])#its convert into list
        Pregnancies=round((values.Pregnancies*100)/17)
        Glucose=round((values.Glucose*100)/200)
        BloodPressure=round((values.BloodPressure*100)/150)
        SkinThickness=round((values.SkinThickness*100)/100)
        Insulin=round((values.Insulin*100)/1000)
        if request.method== 'POST':

            contextt={'Pregnanciess':Pregnancies,'Glucosee':Glucose,'BloodPressuree':BloodPressure,'SkinThicknesss':SkinThickness,
                'Insulinn':Insulin,'BMII':values.BMI,'DiabetesPedigreeFunctionn':values.DiabetesPedigreeFunction,'Agee':values.Age,'check':0    ,'context':context}
               
        else:
             contextt={'Pregnanciess':Pregnancies,'Glucosee':Glucose,'BloodPressuree':BloodPressure,'SkinThicknesss':SkinThickness,
                'Insulinn':Insulin,'BMII':values.BMI,'DiabetesPedigreeFunctionn':values.DiabetesPedigreeFunction,'Agee':values.Age,'check':1    ,'context':context}

        return render(request,'diabetes_graph_com.html',contextt)
    else:
        return redirect('login')

def graph(request):
    if  request.user.is_authenticated:

        if request.method== 'POST':
           global context
            
           return render(request,'diabetesgraph.html',context)


        
    else:      
        return render(request,'login.html')



















# here all function about heart graphs

def previousheart(request):
    if  request.user.is_authenticated:

        listt=[]
        
        current_user = request.user
        current=current_user.id
        #print(type(current))
        curr=User.objects.get(id=current)
        #print(type(curr))
        curr=curr.id
        #print(type(curr))
        values = role_heart.objects.filter(User_id=curr)#its convert into list
    
    
        for value in values.all():
            pp=value.role_heart
            listt.append(pp)
    
        values = heart.objects.get(sno_heart=listt[len(listt)-2])#its convert into list
        trestbps=round((values.trestbps*100)/200)
        chol=round((values.chol*100)/700)
        fbs=round((values.fbs*100)/300)
        thalach=round((values.thalach*100)/250)
        context_heart={'age':values.age,'sex':values.sex,'cp':values.cp,
                    'trestbps':trestbps,'chol':chol,'fbs':fbs,'restecg':values.restecg ,'thalach':thalach,
                    'exang':values.exang,'oldpeak':values.oldpeak,'slope':values.slope,'ca':values.ca,'thal':values.thal}       
        return render(request,'heart_graph.html',context_heart)
        #print(values.BMI)
    else:
                return redirect('login')



def compareheart(request):
    if  request.user.is_authenticated:

        listt=[]
        
        current_user = request.user
        current=current_user.id
        #print(type(current))
        curr=User.objects.get(id=current)
        #print(type(curr))
        curr=curr.id
        #print(type(curr))
        values = role_heart.objects.filter(User_id=curr)#its convert into list
    
    
        for value in values.all():
            pp=value.role_heart
            listt.append(pp)
    
        values = heart.objects.get(sno_heart=listt[len(listt)-2])#its convert into list
        trestbps=round((values.trestbps*100)/200)
        chol=round((values.chol*100)/700)
        fbs=round((values.fbs*100)/300)
        thalach=round((values.thalach*100)/250)
        
        if request.method== 'POST':

             contexttt={'agee':values.age,'sexx':values.sex,'cpp':values.cp,
                    'trestbpss':trestbps,'choll':chol,'fbss':fbs,'restecgg':values.restecg ,'thalachh':thalach,
                    'exangg':values.exang,'oldpeakk':values.oldpeak,'slopee':values.slope,'caa':values.ca,'thall':values.thal,'check':0,'context_heart':context_heart}  
               
        else:
             contexttt={'agee':values.age,'sexx':values.sex,'cpp':values.cp,
                    'trestbpss':trestbps,'choll':chol,'fbss':fbs,'restecgg':values.restecg ,'thalachh':thalach,
                    'exangg':values.exang,'oldpeakk':values.oldpeak,'slopee':values.slope,'caa':values.ca,'thall':values.thal,'check':1,'context_heart':context_heart}  

        return render(request,'heart_graph_com.html',contexttt)
    else:
        return redirect('login')

def graphheart(request):
    if  request.user.is_authenticated:

        if request.method== 'POST':
           global context_heart
            
           return render(request,'heart_graph.html',context_heart)


        
    else:      
        return render(request,'login.html')




    
    
         
    
    


     