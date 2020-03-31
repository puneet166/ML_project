from django.db import models

# Create your models here.
 #class Registration(models.Model):
  #  Firstname=models.CharField(max_length=200)
   # Lastname=models.CharField(max_length=200)
    #EmailId=models.EmailField(max_length=200)
    #HighUser=models.BooleanField(default=False)
    #DateTime=models.DateTimeField()

class diabetes(models.Model):
    Pregnancies=models.IntegerField()
    Glucose=models.IntegerField()
    BloodPressure=models.IntegerField()
    SkinThickness=models.IntegerField()
    Insulin=models.IntegerField()
    BMI=models.IntegerField()
    DiabetesPedigreeFunction=models.IntegerField()
    Age=models.IntegerField()

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
    
    