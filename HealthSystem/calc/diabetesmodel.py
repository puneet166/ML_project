# its model of diabetes apply deep learning  artifical nureal network

import os
import pandas as pd 
#from sklearn.neural_network import MLPClassifier
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import classification_report,confusion_matrix,accuracy_score 
#from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle
import sklearn
from sklearn.externals import joblib
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse


#def preprocessing(df):
 #   X=df.iloc[:,0:8]
  #  Y=df.iloc[:,-1]
    #x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.20)
   # scaler=StandardScaler()
    #scaler.fit(X)
    #scaler.fit(Y)
#    file = open("tranformation_pickle","wb")
 #   pickle.dump(scaler,file)
  #  file.close()
    #with open("tranformation_pickle","wb") as file:
    #pickle.dump(scaler,file)
    #file.close()
  #  x_train=scaler.transform(X)
    #print(x_train)
    #x_test=scaler.transform(x_test)
    #return x_train,x_test


#def training(x_train,y_train):
 #   mlp=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(22,22,22),max_iter=50,activation='logistic')
  #  mlp.fit(x_train,Y)
    #with open("model_pickle","wb") as f:
    #pickle.dump(mlp,f)
   # file1 = open("model_pickle","wb")
    #pickle.dump(mlp,file1)
   # file1.close()
    

def prediction(da):
    
        scalerr=joblib.load(r"C:\Users\Puneet Singh\projects\HealthSystem\calc\tranformation_pickle.pkl")
        model=joblib.load(r"C:\Users\Puneet Singh\projects\HealthSystem\calc\model_pickle.pkl")
        ar=scalerr.transform(da)
        predictions=model.predict(ar)
        return predictions
        
    
        #mydata=da.data
        #print(type(da))
        #print("poiuygfm,")
        #unit=np.array(list(mydata.values()))
        #da=unit.reshape(1,-1)
        # x=obj.to_dict()
        #x = [[1,85,66,29,0,26.6,0.351,31]]
        #da = pd.DataFrame(x,index=[0])
        #pkl_filename="tranformation_pickle.pkl" #file name
        #pkl_filename=os.path.dirname(__file__) + "/" + pkl_filename #first do this in django for access file
        #file3 = open(pkl_filename,'rb')# now read pickle

        #scalerr = pickle.load(file3)
        #file.close()
        #print(da)
        #with open("tranformation_pickle","rb") as file:
        #scaler=pickle.load(file)
             
        #pkl_filename1="model_pickle.pkl"
        #pkl_filename1=os.path.dirname(__file__) + "/" + pkl_filename1
    
        #file4 = open(pkl_filename1,'rb')
        #model = pickle.load(file4)
        #with open("model_pickle","rb") as f:
        #model=pickle.load(f)
             
        #df=pd.read_csv('diabetes.csv')

        #preprocessing(df)
        #training(x,y)
        #prediction()
        #newf=pd.DataFrame(predictions)
        #newf=newf.replace({0:"no",1:"yes"})
        #return('your status is {}',format(newf))
        #except ValueError as e:
            #return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
    
     