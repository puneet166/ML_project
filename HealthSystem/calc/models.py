from django.db import models
from django.contrib.auth.models import User





# Create your models here. its model mean table will created in database
 #class Registration(models.Model):
  #  Firstname=models.CharField(max_length=200)
   # Lastname=models.CharField(max_length=200)
    #EmailId=models.EmailField(max_length=200)
    #HighUser=models.BooleanField(default=False)
    #DateTime=models.DateTimeField()

class diabetes(models.Model):
    sno=models.AutoField(primary_key=True)
    Pregnancies=models.IntegerField()
    Glucose=models.IntegerField()
    BloodPressure=models.IntegerField()
    SkinThickness=models.IntegerField()
    Insulin=models.IntegerField()
    BMI=models.FloatField()
    DiabetesPedigreeFunction=models.FloatField()
    Age=models.IntegerField()
    Outcome=models.IntegerField(default=2)
    

    #now convert into dic for deal with dataframe in pandas

def to_dict(self):
    return{
        'Pregnancies':self.Pregnancies,
        'Glucose':self.Glucose,
        'BloodPressure':self.BloodPressure,
        'SkinThickness':self.SkinThickness,
        'Insulin':self.Insulin,
        'BMI':self.BMI,
        'DiabetesPedigreeFunction':self.DiabetesPedigreeFunction,
        'Age':self.Age
            }    

class heart(models.Model):
    sno_heart=models.AutoField(primary_key=True)
    age=models.IntegerField()
    sex=models.IntegerField()
    cp=models.IntegerField()
    trestbps=models.IntegerField()
    chol=models.IntegerField()
    fbs=models.IntegerField()
    restecg=models.IntegerField()
    thalach=models.IntegerField()
    exang=models.IntegerField()
    oldpeak=models.FloatField()
    slope=models.IntegerField()
    ca=models.IntegerField()
    thal=models.IntegerField()
    target=models.IntegerField(default=2)
class role(models.Model):
    

    role_dia=models.IntegerField()
    User_mail=models.IntegerField()


class query(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Message=models.CharField(max_length=1000)
    



    
    
    