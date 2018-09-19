from flask import Flask
from flask import render_template,request
from datetime import time
  
 
import tensorflow as tf  
import pandas as pd  
import numpy as np     
 
import matplotlib.pyplot as plt    
import tensorflow.contrib.rnn as rnn
import tensorflow.contrib.layers as tflayers

from sklearn.preprocessing import MinMaxScaler
  
import math     
import datetime  
 
		   
app = Flask(__name__)   

@app.route("/")  
def main():
    return render_template('main.html')

@app.route("/line_chart",methods=['POST','GET']) 
def line_chart():  
    number = request.form.get('ejemplo',type=int)
    fullPath='C:/Users/USUARIO/Documents/stocksModel/predicciones/'
    remainingPath='prediccion'+str(number)+'.csv' 
    df=pd.read_csv(fullPath+remainingPath,header=0) 
    prediccion=df['prediccion']    
    real=df['real']    
    fecha=df['fecha']      
    precios=df['precios']	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    interpretacion1={}
    interpretacion1[0]="El modelo sugiere que la tasa de cambio podria ser negativa entre el 08-08-2018. Esto implicaria que:"
    interpretacion1[1]=""
    interpretacion1[2]=""
    interpretacion1[3]="Si el precio de cierre del 30-07-2018 fue de 15.95, el precio de cierre del 08-08-2018 podria ser menor a 15.95 con una tasa de cambio posiblemente cercana a -1.91."
    interpretacion1[4]="Si el precio de cierre del 31-07-2018 fue de 15.97, el precio de cierre del 09-08-2018 podria ser menor a 15.97 con una tasa de cambio posiblemente cercana a -1.97."
    interpretacion1[5]="Si el precio de cierre del 01-08-2018 fue de 15.80, el precio de cierre del 10-08-2018 podria ser menor a 15.80 con una tasa de cambio posiblemente cercana a -2.21."
    interpretacion1[6]="Si el precio de cierre del 02-08-2018 fue de 15.70, el precio de cierre del 13-08-2018 podria ser menor a 15.70 con una tasa de cambio posiblemente cercana a -2.17."
    interpretacion1[7]="Si el precio de cierre del 03-08-2018 fue de 15.72, el precio de cierre del 14-08-2018 podria ser menor a 15.72 con una tasa de cambio posiblemente cercana a -2.98."   
    interpretacion2={}
    interpretacion2[0]="El modelo sugiere que la tasa de cambio podria ser negativa entre el 15-08-2018 y el 17-08-2018, y positiva entre el 20-08-2018 y el 21-08-2018. Esto implicaria que:"
    interpretacion2[1]=""
    interpretacion2[2]=""
    interpretacion2[3]="Si el precio de cierre del 06-08-2018 fue de 15.72, el precio de cierre del 15-08-2018 podria ser menor a 15.72 con una tasa de cambio posiblemente cercana a -0.38."
    interpretacion2[4]="Si el precio de cierre del 07-08-2018 fue de 16.17, el precio de cierre del 16-08-2018 podria ser menor a 16.17 con una tasa de cambio posiblemente cercana a -0.60."
    interpretacion2[5]="Si el precio de cierre del 08-08-2018 fue de 16.27, el precio de cierre del 17-08-2018 podria ser menor a 16.27 con una tasa de cambio posiblemente cercana a -0.78."
    interpretacion2[6]="Si el precio de cierre del 09-08-2018 fue de 15.04, el precio de cierre del 20-08-2018 podria ser mayor a 15.04 con una tasa de cambio posiblemente cercana a 1.18."
    interpretacion2[7]="Si el precio de cierre del 10-08-2018 fue de 15.66, el precio de cierre del 21-08-2018 podria ser mayor a 15.66 con una tasa de cambio posiblemente cercana a 3.07."
    interpretacion3={}
    interpretacion3[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 21-08-2018. Esto implicaria que:"
    interpretacion3[1]=""
    interpretacion3[2]="Si el precio de cierre del 10-08-2018 fue de 15.66, el precio de cierre del 21-08-2018 podria ser mayor a 15.66 con una tasa de cambio posiblemente cercana a 5.49."
    interpretacion3[3]="Si el precio de cierre del 13-08-2018 fue de 15.78, el precio de cierre del 22-08-2018 podria ser mayor a 15.78 con una tasa de cambio posiblemente cercana a 3.59."
    interpretacion3[4]="Si el precio de cierre del 14-08-2018 fue de 15.90, el precio de cierre del 23-08-2018 podria ser mayor a 15.90 con una tasa de cambio posiblemente cercana a 1.47."
    interpretacion3[5]="Si el precio de cierre del 15-08-2018 fue de 15.71, el precio de cierre del 24-08-2018 podria ser mayor a 15.71 con una tasa de cambio posiblemente cercana a 1.11."
    interpretacion3[6]="Si el precio de cierre del 16-08-2018 fue de 15.58, el precio de cierre del 27-08-2018 podria ser mayor a 15.58 con una tasa de cambio posiblemente cercana a 3.46."
    interpretacion3[7]="Si el precio de cierre del 17-08-2018 fue de 15.72, el precio de cierre del 28-08-2018 podria ser mayor a 15.72 con una tasa de cambio posiblemente cercana a 3.72."
    interpretacion4={}
    interpretacion4[0]="El modelo sugiere que la tasa de cambio podria ser negativa aproximadamente a partir del 29-08-2018. Esto implicaria que:"
    interpretacion4[1]=""
    interpretacion4[2]=""
    interpretacion4[3]="Si el precio de cierre del 20-08-2018 fue de 15.98, el precio de cierre del 29-08-2018 podria ser menor a 15.98 con una tasa de cambio posiblemente cercana a -3.83."
    interpretacion4[4]="Si el precio de cierre del 21-08-2018 fue de 16.41, el precio de cierre del 30-08-2018 podria ser menor a 16.41 con una tasa de cambio posiblemente cercana a -5.05."
    interpretacion4[5]="Si el precio de cierre del 22-08-2018 fue de 16.42, el precio de cierre del 31-08-2018 podria ser menor a 16.42 con una tasa de cambio posiblemente cercana a -4.54." 
    interpretacion4[6]="Si el precio de cierre del 23-08-2018 fue de 16.02, el precio de cierre del 03-09-2018 podria ser menor a 16.02 con una tasa de cambio posiblemente cercana a -4.55."  
    interpretacion4[7]="Si el precio de cierre del 24-08-2018 fue de 16.13, el precio de cierre del 04-09-2018 podria ser menor a 16.13 con una tasa de cambio posiblemente cercana a -5.61." 	
    interpretacion5={}
    interpretacion5[0]="El modelo sugiere que la tasa de cambio podria ser negativa aproximadamente a partir del 05-09-2018. Esto implicaria que:"
    interpretacion5[1]=""
    interpretacion5[2]=""
    interpretacion5[3]="Si el precio de cierre del 27-08-2018 fue de 16.32, el precio de cierre del 05-09-2018 podria ser menor a 16.32 con una tasa de cambio posiblemente cecana a -1.61."
    interpretacion5[4]="Si el precio de cierre del 28-08-2018 fue de 16.37, el precio de cierre del 06-09-2018 podria ser menor a 16.37 con una tasa de cambio posiblemente cecana a -2.85."
    interpretacion5[5]="Si el precio de cierre del 29-08-2018 fue de 16.55, el precio de cierre del 07-09-2018 podria ser menor a 16.55 con una tasa de cambio posiblemente cecana a -3.95."
    interpretacion5[6]="Si el precio de cierre del 30-08-2018 fue de 16.22, el precio de cierre del 10-09-2018 podria ser menor a 16.22 con una tasa de cambio posiblemente cecana a -3.84."  
    interpretacion5[7]="Si el precio de cierre del 31-08-2018 fue de 16.05, el precio de cierre del 11-09-2018 podria ser menor a 16.05 con una tasa de cambio posiblemente cecana a -3.91."  
    interpretacion6={}
    interpretacion6[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 13-09-2018 aproximadamente. Eso implicaria que:"
    interpretacion6[1]=""
    interpretacion6[2]="" 
    interpretacion6[3]=""  
    interpretacion6[4]="Si el precio de cierre del 04-09-2018 fue de 15.79, el precio de cierre del 13-09-2018 podria ser mayor a 15.79 con una tasa de cambio posiblemente cercana a 1.74."
    interpretacion6[5]="Si el precio de cierre del 05-09-2018 fue de 15.30, el precio de cierre del 14-09-2018 podria ser mayor a 15.30 con una tasa de cambio posiblemente cercana a 1.96."
    interpretacion6[6]="Si el precio de cierre del 06-09-2018 fue de 15.51, el precio de cierre del 17-09-2018 podria ser mayor a 15.51 con una tasa de cambio posiblemente cercana a 0.60."
    interpretacion6[7]="Si el precio de cierre del 07-09-2018 fue de 15.71, el precio de cierre del 18-09-2018 podria ser mayor a 15.71 con una tasa de cambio posiblemente cercana a 0.75."
    interpretaciones=["dummy",interpretacion1,interpretacion2,interpretacion3,interpretacion4,interpretacion5,interpretacion6]
    interpretacion=interpretaciones[number]
    dataframe1=pd.DataFrame({'fecha':["08-08-2018","09-08-2018","10-08-2018","13-08-2018","14-08-2018"],'precio de cierre':["16.27","15.94","15.66","15.78","15.9"],'tasa de cambio':["2.00","-0.18","-0.88","0.50","1.14"],'acierto del modelo':["no","si","si","no","no"]})
    dataframe1=dataframe1[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframe2=pd.DataFrame({'fecha':["15-08-2018","16-08-2018","17-08-2018","20-08-2018","21-08-2018"],'precio de cierre':["15.71","15.58","15.72","15.98","16.41"],'tasa de cambio':["-0.06","-3.64","-3.38","0.25","4.78"],'acierto del modelo':["si","si","si","si","si"]})
    dataframe2=dataframe2[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframe3=pd.DataFrame({'fecha':["21-08-2018","22-08-2018","23-08-2018","24-08-2018","27-08-2018","28-08-2018"],'precio de cierre':["16.41","16.42","16.02","16.13","16.32","16.37"],'tasa de cambio':["4.78","4.05","0.75","2.67","4.74","4.13"],'acierto del modelo':["si","si","si","si","si","si"]})
    dataframe3=dataframe3[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframe4=pd.DataFrame({'fecha':["29-08-2018","30-08-2018","31-08-2018","03-09-2018","04-09-2018"],'precio de cierre':["16.55","16.22","16.05","16.10","15.79"],'tasa de cambio':["3.56","-1.15","-2.25","0.49","-2.10"],'acierto del modelo':["no","si","si","no","si"]})
    dataframe4=dataframe4[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframe5=pd.DataFrame({'fecha':["05-09-2018","06-09-2018","07-09-2018","10-09-2018","11-09-2018"],'precio de cierre':["15.30","15.51","15.71","15.71","15.60"],'tasa de cambio':["-6.24","-5.25","-5.07","-3.14","-2.80"],'acierto del modelo':["si","si","si","si","si"]})
    dataframe5=dataframe5[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframe6=pd.DataFrame({'fecha':["13-09-2018","14-09-2018","17-09-2018","18-09-2018"],'precio de cierre':["16.06","15.64","15.55",""],'tasa de cambio':["1.70","2.22","0.25",""],'acierto del modelo':["si","si","si",""]})
    dataframe6=dataframe6[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframes=["dummy",dataframe1,dataframe2,dataframe3,dataframe4,dataframe5,dataframe6]
    x=dataframes[number]
    return render_template('line_chart.html', values_prediccion=prediccion,values_real=real,values_precios=precios, labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],interpretacion=interpretacion)
 
@app.route("/last_batch",methods=['POST','GET'])	
def last_batch():   
    interpretacion={} 
    interpretacion[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 20-09-2018 aproximadamente. Eso implicaria que:"
    interpretacion[1]="" 
    interpretacion[2]="" 
    interpretacion[3]=""
    interpretacion[4]="Si el precio de cierre del 11-09-2018 fue de 15.60, el precio de cierre del 20-09-2018 podria ser mayor a 15.60 con una tasa de cambio posiblemente cercana a 0.32."
    interpretacion[5]="Si el precio de cierre del 12-09-2018 fue de 16.05, el precio de cierre del 21-09-2018 podria ser mayor a 16.05 con una tasa de cambio posiblemente cercana a 2.41."
    interpretacion[6]="Si el precio de cierre del 13-09-2018 fue de 16.06, el precio de cierre del 24-09-2018 podria ser mayor a 16.06 con una tasa de cambio posiblemente cercana a 4.17."
    interpretacion[7]="Si el precio de cierre del 14-09-2018 fue de 15.64, el precio de cierre del 25-09-2018 podria ser mayor a 15.64 con una tasa de cambio posiblemente cercana a 3.65."
    fullPath='C:/Users/USUARIO/Documents/stocksModel/predicciones/'
    remainingPath='prediccionFinal.csv'
    df=pd.read_csv(fullPath+remainingPath,header=0)
    prediccion=df['prediccion'] 
    real=df['real']
    fecha=df['fecha']  
    fecha=[str(i) for i in fecha]
    precios=df['precios']
    fechaInicio=fecha[0]
    fechaFin=fecha[6]
    x=pd.DataFrame({'fecha':["20-09-2018","21-09-2018","24-09-2018","25-09-2018"],'precio de cierre':["","","",""],'tasa de cambio':["","","",""],'acierto del modelo':["","","",""]})
    x=x[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    return render_template('last_batch.html', values_prediccion=prediccion,values_real=real,values_precios=precios, labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],interpretacion=interpretacion)
   

   
if __name__ == "__main__":
    app.run(debug=True,port=5000)
#host='0.0.0.0'	
print('You can check the website now!')