from flask import Flask
from flask import render_template,request
from datetime import time
   
import pandas as pd  
import numpy as np     
 
import matplotlib.pyplot as plt    

import math     
import datetime  
 
		   
app = Flask(__name__)   

@app.route("/")  
def main():
    return render_template('main.html')

@app.route("/line_chart",methods=['POST','GET']) 
def line_chart():  
    number = request.form.get('ejemplo',type=int)
    fullPath='model/predicciones/'
    remainingPath='prediccion'+str(number)+'.csv' 
    df=pd.read_csv(fullPath+remainingPath,header=0) 
    prediccion=df['prediccion']    
    real=df['real']    
    fecha=df['fecha']      
    precios=df['precios']	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    interpretacion1={}
    interpretacion1[0]="El modelo sugiere que la tasa de cambio podria negativa a partir del 06-08-2018 excepto entre el 06-08-2018 y 07-08-2018, y el 14-08-2018. Esto implicaria que:"
    interpretacion1[1]="Si el precio de cierre del 26-07-2018 fue de 15.86, el precio de cierre del 06-08-2018 podria ser mayor a 15.86 con una tasa de cambio posiblemente cercana a 1.05."
    interpretacion1[2]="Si el precio de cierre del 27-07-2018 fue de 15.88, el precio de cierre del 07-08-2018 podria ser mayor a 15.88 con una tasa de cambio posiblemente cercana a 0.64."
    interpretacion1[3]="Si el precio de cierre del 30-07-2018 fue de 15.95, el precio de cierre del 08-08-2018 podria ser menor a 15.95 con una tasa de cambio posiblemente cercana a -2.01."
    interpretacion1[4]="Si el precio de cierre del 31-07-2018 fue de 15.97, el precio de cierre del 09-08-2018 podria ser menor a 15.97 con una tasa de cambio posiblemente cercana a -2.87."
    interpretacion1[5]="Si el precio de cierre del 01-08-2018 fue de 15.80, el precio de cierre del 10-08-2018 podria ser menor a 15.80 con una tasa de cambio posiblemente cercana a -2.35."
    interpretacion1[6]="Si el precio de cierre del 02-08-2018 fue de 15.70, el precio de cierre del 13-08-2018 podria ser menor a 15.70 con una tasa de cambio posiblemente cercana a -0.78."
    interpretacion1[7]="Si el precio de cierre del 03-08-2018 fue de 15.72, el precio de cierre del 14-08-2018 podria ser mayor a 15.72 con una tasa de cambio posiblemente cercana a 0.09."   
    interpretacion2={}
    interpretacion2[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 13-08-2018 excepto entre el 16-08-2018 y 17-08-2018. Esto implicaria que:"
    interpretacion2[1]="Si el precio de cierre del 02-08-2018 fue de 15.70, el precio de cierre del 13-08-2018 podria ser mayor a 15.70 con una tasa de cambio posiblemente cercana a 0.86."
    interpretacion2[2]="Si el precio de cierre del 03-08-2018 fue de 15.72, el precio de cierre del 14-08-2018 podria ser mayor a 15.72 con una tasa de cambio posiblemente cercana a 1.05."
    interpretacion2[3]="Si el precio de cierre del 06-08-2018 fue de 15.72, el precio de cierre del 15-08-2018 podria ser mayor a 15.72 con una tasa de cambio posiblemente cercana a 0.11."
    interpretacion2[4]="Si el precio de cierre del 07-08-2018 fue de 16.17, el precio de cierre del 16-08-2018 podria ser menor a 16.17 con una tasa de cambio posiblemente cercana a -0.20."
    interpretacion2[5]="Si el precio de cierre del 08-08-2018 fue de 16.27, el precio de cierre del 17-08-2018 podria ser menor a 16.27 con una tasa de cambio posiblemente cercana a -0.21."
    interpretacion2[6]="Si el precio de cierre del 09-08-2018 fue de 15.04, el precio de cierre del 20-08-2018 podria ser mayor a 15.04 con una tasa de cambio posiblemente cercana a 1.29."
    interpretacion2[7]="Si el precio de cierre del 10-08-2018 fue de 15.66, el precio de cierre del 21-08-2018 podria ser mayor a 15.66 con una tasa de cambio posiblemente cercana a 2.61."
    interpretacion3={}
    interpretacion3[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 20-08-2018. Esto implicaria que:"
    interpretacion3[1]="Si el precio de cierre del 09-08-2018 fue de 15.94, el precio de cierre del 20-08-2018 podria ser mayor a 15.94 con una tasa de cambio posiblemente cercana a 2.22."
    interpretacion3[2]="Si el precio de cierre del 10-08-2018 fue de 15.66, el precio de cierre del 21-08-2018 podria ser mayor a 15.66 con una tasa de cambio posiblemente cercana a 4.14."
    interpretacion3[3]="Si el precio de cierre del 13-08-2018 fue de 15.78, el precio de cierre del 22-08-2018 podria ser mayor a 15.78 con una tasa de cambio posiblemente cercana a 2.69."
    interpretacion3[4]="Si el precio de cierre del 14-08-2018 fue de 15.90, el precio de cierre del 23-08-2018 podria ser mayor a 15.90 con una tasa de cambio posiblemente cercana a 1.06."
    interpretacion3[5]="Si el precio de cierre del 15-08-2018 fue de 15.71, el precio de cierre del 24-08-2018 podria ser mayor a 15.71 con una tasa de cambio posiblemente cercana a 0.88."
    interpretacion3[6]="Si el precio de cierre del 16-08-2018 fue de 15.58, el precio de cierre del 27-08-2018 podria ser mayor a 15.58 con una tasa de cambio posiblemente cercana a 2.54."
    interpretacion3[7]="Si el precio de cierre del 17-08-2018 fue de 15.72, el precio de cierre del 28-08-2018 podria ser mayor a 15.72 con una tasa de cambio posiblemente cercana a 2.79."
    interpretacion4={}
    interpretacion4[0]="El modelo sugiere que la tasa de cambio podria ser negativa entre el 27-08-2018 y 31-09-2018, y positiva entre el 03-09-2018 y 04-09-2018. Esto implicaria que:"
    interpretacion4[1]="Si el precio de cierre del 16-08-2018 fue de 15.58, el precio de cierre del 27-08-2018 podria ser menor a 15.95 con una tasa de cambio posiblemente cercana a -0.63."
    interpretacion4[2]="Si el precio de cierre del 17-08-2018 fue de 15.72, el precio de cierre del 28-08-2018 podria ser menor a 15.72 con una tasa de cambio posiblemente cercana a -1.14."
    interpretacion4[3]="Si el precio de cierre del 20-08-2018 fue de 15.98, el precio de cierre del 29-08-2018 podria ser menor a 15.98 con una tasa de cambio posiblemente cercana a -1.74."
    interpretacion4[4]="Si el precio de cierre del 21-08-2018 fue de 16.41, el precio de cierre del 30-08-2018 podria ser menor a 16.41 con una tasa de cambio posiblemente cercana a -1.72."
    interpretacion4[5]="Si el precio de cierre del 22-08-2018 fue de 16.42, el precio de cierre del 31-08-2018 podria ser menor a 16.42 con una tasa de cambio posiblemente cercana a -1.10." 
    interpretacion4[6]="Si el precio de cierre del 23-08-2018 fue de 16.02, el precio de cierre del 03-09-2018 podria ser mayor a 16.02 con una tasa de cambio posiblemente cercana a 0.13."  
    interpretacion4[7]="Si el precio de cierre del 24-08-2018 fue de 16.13, el precio de cierre del 04-09-2018 podria ser mayor a 16.13 con una tasa de cambio posiblemente cercana a 0.80." 	
    interpretacion5={}
    interpretacion5[0]="El modelo sugiere que la tasa de cambio podria ser positiva el 03-09-2018 y negativa a partir del 04-09-2018. Esto implicaria que:"
    interpretacion5[1]="Si el precio de cierre del 23-08-2018 fue de 16.02, el precio de cierre del 03-09-2018 podria ser mayor a 16.02 con una tasa de cambio posiblemente cecana a 0.17."
    interpretacion5[2]="Si el precio de cierre del 24-08-2018 fue de 16.13, el precio de cierre del 04-09-2018 podria ser menor a 16.13 con una tasa de cambio posiblemente cecana a -0.48."
    interpretacion5[3]="Si el precio de cierre del 27-08-2018 fue de 16.32, el precio de cierre del 05-09-2018 podria ser menor a 16.32 con una tasa de cambio posiblemente cecana a -1.47."
    interpretacion5[4]="Si el precio de cierre del 28-08-2018 fue de 16.37, el precio de cierre del 06-09-2018 podria ser menor a 16.37 con una tasa de cambio posiblemente cecana a -2.19."
    interpretacion5[5]="Si el precio de cierre del 29-08-2018 fue de 16.55, el precio de cierre del 07-09-2018 podria ser menor a 16.55 con una tasa de cambio posiblemente cecana a -2.79."
    interpretacion5[6]="Si el precio de cierre del 30-08-2018 fue de 16.22, el precio de cierre del 10-09-2018 podria ser menor a 16.22 con una tasa de cambio posiblemente cecana a -2.81."  
    interpretacion5[7]="Si el precio de cierre del 31-08-2018 fue de 16.05, el precio de cierre del 11-09-2018 podria ser menor a 16.05 con una tasa de cambio posiblemente cecana a -2.95."  
    interpretacion6={}
    interpretacion6[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 10-09-2018 aproximadamente. Eso implicaria que:"
    interpretacion6[1]="Si el precio de cierre del 30-08-2018 fue de 16.22, el precio de cierre del 10-09-2018 podria ser mayor a 16.22 con una tasa de cambio posiblemente cercana a 0.78."
    interpretacion6[2]="Si el precio de cierre del 31-08-2018 fue de 16.05, el precio de cierre del 11-09-2018 podria ser mayor a 16.05 con una tasa de cambio posiblemente cercana a 2.89." 
    interpretacion6[3]="Si el precio de cierre del 03-09-2018 fue de 16.10, el precio de cierre del 12-09-2018 podria ser mayor a 16.10 con una tasa de cambio posiblemente cercana a 2.89."  
    interpretacion6[4]="Si el precio de cierre del 04-09-2018 fue de 15.79, el precio de cierre del 13-09-2018 podria ser mayor a 15.79 con una tasa de cambio posiblemente cercana a 3.66."
    interpretacion6[5]="Si el precio de cierre del 05-09-2018 fue de 15.30, el precio de cierre del 14-09-2018 podria ser mayor a 15.30 con una tasa de cambio posiblemente cercana a 2.04."
    interpretacion6[6]="Si el precio de cierre del 06-09-2018 fue de 15.51, el precio de cierre del 17-09-2018 podria ser mayor a 15.51 con una tasa de cambio posiblemente cercana a 1.77."
    interpretacion6[7]="Si el precio de cierre del 07-09-2018 fue de 15.71, el precio de cierre del 18-09-2018 podria ser mayor a 15.71 con una tasa de cambio posiblemente cercana a 3.73."
    interpretaciones=["dummy",interpretacion1,interpretacion2,interpretacion3,interpretacion4,interpretacion5,interpretacion6]
    interpretacion=interpretaciones[number]
    dataframe1=pd.DataFrame({'fecha':["06-08-2018","07-08-2018","08-08-2018","09-08-2018","10-08-2018","13-08-2018","14-08-2018"],'precio de cierre':["15.72","16.17","16.27","15.94","15.66","15.78","15.9"],'tasa de cambio':["","","2.00","-0.18","-0.88","0.50","1.14"],'acierto del modelo':["no","si","no","si","si","no","si"]})
    dataframe1=dataframe1[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframe2=pd.DataFrame({'fecha':["13-08-2018","14-08-2018","15-08-2018","16-08-2018","17-08-2018","20-08-2018","21-08-2018"],'precio de cierre':["15.78","15.90","15.71","15.58","15.72","15.98","16.41"],'tasa de cambio':["","","-0.06","-3.64","-3.38","0.25","4.78"],'acierto del modelo':["si","si","no","si","si","si","si"]})
    dataframe2=dataframe2[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframe3=pd.DataFrame({'fecha':["20-08-2018","21-08-2018","22-08-2018","23-08-2018","24-08-2018","27-08-2018","28-08-2018"],'precio de cierre':["15.98","16.41","16.42","16.02","16.13","16.32","16.37"],'tasa de cambio':["4.78","4.05","0.75","2.67","4.74","4.13",""],'acierto del modelo':["si","si","si","si","si","si","si"]})
    dataframe3=dataframe3[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframe4=pd.DataFrame({'fecha':["27-08-2018","28-08-2018","29-08-2018","30-08-2018","31-08-2018","03-09-2018","04-09-2018"],'precio de cierre':["16.32","16.37","16.55","16.22","16.05","16.10","15.79"],'tasa de cambio':["","","","","","",""],'acierto del modelo':["no","no","no","si","si","si","no"]})
    dataframe4=dataframe4[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframe5=pd.DataFrame({'fecha':["03-09-2018","04-09-2018","05-09-2018","06-09-2018","07-09-2018","10-09-2018","11-09-2018"],'precio de cierre':["16.10","15.79","15.30","15.51","15.71","15.71","15.60"],'tasa de cambio':["","","","","","",""],'acierto del modelo':["si","si","si","si","si","si","si"]})
    dataframe5=dataframe5[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframe6=pd.DataFrame({'fecha':["10-09-2018","11-09-2018","12-09-2018","13-09-2018","14-09-2018","17-09-2018","18-09-2018"],'precio de cierre':["15.71","15.60","16.05","16.06","15.67","15.55","15.61"],'tasa de cambio':["-3.14","-2.80","-0.31","1.70","2.41","0.25","-0.63"],'acierto del modelo':["no","no","no","si","si","si","no"]})
    dataframe6=dataframe6[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    dataframes=["dummy",dataframe1,dataframe2,dataframe3,dataframe4,dataframe5,dataframe6]
    x=dataframes[number]
    x=x.iloc[3:,]
    return render_template('line_chart.html', values_prediccion=prediccion,values_real=real,values_precios=precios, labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],interpretacion=interpretacion)
 
@app.route("/last_batch",methods=['POST','GET'])	
def last_batch():   
    interpretacion={} 
    interpretacion[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 17-09-2018 aproximadamente. Eso implicaria que:"
    interpretacion[1]="Si el precio de cierre del 06-09-2018 fue de 15.51, el precio de cierre del 17-09-2018 podria ser mayor a 15.51 con una tasa de cambio posiblemente cercana a 0.66." 
    interpretacion[2]="Si el precio de cierre del 07-09-2018 fue de 15.71, el precio de cierre del 18-09-2018 podria ser mayor a 15.71 con una tasa de cambio posiblemente cercana a 0.72." 
    interpretacion[3]="Si el precio de cierre del 10-09-2018 fue de 15.71, el precio de cierre del 19-09-2018 podria ser mayor a 15.71 con una tasa de cambio posiblemente cercana a 1.24."
    interpretacion[4]="Si el precio de cierre del 11-09-2018 fue de 15.60, el precio de cierre del 20-09-2018 podria ser mayor a 15.60 con una tasa de cambio posiblemente cercana a 0.63."
    interpretacion[5]="Si el precio de cierre del 12-09-2018 fue de 16.05, el precio de cierre del 21-09-2018 podria ser mayor a 16.05 con una tasa de cambio posiblemente cercana a 1.90."
    interpretacion[6]="Si el precio de cierre del 13-09-2018 fue de 16.06, el precio de cierre del 24-09-2018 podria ser mayor a 16.06 con una tasa de cambio posiblemente cercana a 2.03."
    interpretacion[7]="Si el precio de cierre del 14-09-2018 fue de 15.67, el precio de cierre del 25-09-2018 podria ser mayor a 15.67 con una tasa de cambio posiblemente cercana a 1.90."
    fullPath='model/predicciones/'
    remainingPath='prediccionFinal.csv'
    df=pd.read_csv(fullPath+remainingPath,header=0)
    prediccion=df['prediccion'] 
    real=df['real']
    fecha=df['fecha']  
    fecha=[str(i) for i in fecha]
    precios=df['precios']
    fechaInicio=fecha[0]
    fechaFin=fecha[6]
    x=pd.DataFrame({'fecha':["17-09-2018","18-09-2018","19-09-2018","20-09-2018","21-09-2018","24-09-2018","25-09-2018"],'precio de cierre':["15.55","15.61","15.60","","","",""],'tasa de cambio':["0.25","-0.63","-0.70","","","",""],'acierto del modelo':["si","no","no","","","",""]})
    x=x[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    x=x.iloc[3:,]
    return render_template('last_batch.html', values_prediccion=prediccion,values_real=real,values_precios=precios, labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],interpretacion=interpretacion)
   

   
if __name__ == "__main__":
    #app.run(debug=True,port=5000)
	app.run(debug=True)
print('You can check the website now!')