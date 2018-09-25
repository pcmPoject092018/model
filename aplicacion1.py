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
    dataframe1=pd.read_csv("model/dataframe1.csv",header=0)
    dataframe2=pd.read_csv("model/dataframe2.csv",header=0)
    dataframe3=pd.read_csv("model/dataframe3.csv",header=0)
    dataframe4=pd.read_csv("model/dataframe4.csv",header=0)
    dataframe5=pd.read_csv("model/dataframe5.csv",header=0)
    dataframe6=pd.read_csv("model/dataframe6.csv",header=0)
    dataframe7=pd.read_csv("model/dataframe7.csv",header=0)
    dataframe1previous=pd.read_csv("model/dataframe1previous.csv",header=0)
    dataframe2previous=pd.read_csv("model/dataframe2previous.csv",header=0)
    dataframe3previous=pd.read_csv("model/dataframe3previous.csv",header=0)
    dataframe4previous=pd.read_csv("model/dataframe4previous.csv",header=0)
    dataframe5previous=pd.read_csv("model/dataframe5previous.csv",header=0)
    dataframe6previous=pd.read_csv("model/dataframe6previous.csv",header=0)
    dataframe7previous=pd.read_csv("model/dataframe7previous.csv",header=0)
    dataframe1["acierto del modelo"]=["","","","si","si","no","si"]
    dataframe2["acierto del modelo"]=["","","","si","si","si","si"]	
    dataframe3["acierto del modelo"]=["","","","si","si","si","si"]	
    dataframe4["acierto del modelo"]=["","","","si","si","si","no"]	
    dataframe5["acierto del modelo"]=["","","","si","si","si","si"]	
    dataframe6["acierto del modelo"]=["","","","si","si","si","no"]
    dataframe7["acierto del modelo"]=["","","","si","no","no",float('NaN')]	
    dataframes=["dummy",dataframe1,dataframe2,dataframe3,dataframe4,dataframe5,dataframe6,dataframe7]
    x=dataframes[number]
    x=x.iloc[3:,].reset_index(drop=True) #ultimos 4 pronosticos
    x=x.iloc[::-1]	
    interpretacion1={}
    interpretacion1[0]="El modelo sugiere que la tasa de cambio podria ser negativa a partir del 09-08-2018 excepto el 14-08-2018. Esto implicaria que:"
    interpretacion1[1]="Si el precio de cierre del " + str(dataframe1previous["fecha"][0]) + " fue de " + str(dataframe1previous["precios"][0]) + ", el precio de cierre del " + str(dataframe1["fecha"][0]) + " podria ser mayor a " + str(dataframe1previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion1[2]="Si el precio de cierre del " + str(dataframe1previous["fecha"][1]) + " fue de " + str(dataframe1previous["precios"][1]) + ", el precio de cierre del " + str(dataframe1["fecha"][1]) + " podria ser mayor a " + str(dataframe1previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion1[3]="Si el precio de cierre del " + str(dataframe1previous["fecha"][2]) + " fue de " + str(dataframe1previous["precios"][2]) + ", el precio de cierre del " + str(dataframe1["fecha"][2]) + " podria ser menor a " + str(dataframe1previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion1[4]="Si el precio de cierre del " + str(dataframe1previous["fecha"][3]) + " fue de " + str(dataframe1previous["precios"][3]) + ", el precio de cierre del " + str(dataframe1["fecha"][3]) + " podria ser menor a " + str(dataframe1previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion1[5]="Si el precio de cierre del " + str(dataframe1previous["fecha"][4]) + " fue de " + str(dataframe1previous["precios"][4]) + ", el precio de cierre del " + str(dataframe1["fecha"][4]) + " podria ser menor a " + str(dataframe1previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion1[6]="Si el precio de cierre del " + str(dataframe1previous["fecha"][5]) + " fue de " + str(dataframe1previous["precios"][5]) + ", el precio de cierre del " + str(dataframe1["fecha"][5]) + " podria ser menor a " + str(dataframe1previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion1[7]="Si el precio de cierre del " + str(dataframe1previous["fecha"][6]) + " fue de " + str(dataframe1previous["precios"][6]) + ", el precio de cierre del " + str(dataframe1["fecha"][6]) + " podria ser mayor a " + str(dataframe1previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13]) 
    interpretacion2={}
    interpretacion2[0]="El modelo sugiere que la tasa de cambio podria ser negativa el 16-08-2018, 17-08-2918 y positiva el 20-08-2018, 21-08-2018. Esto implicaria que:"
    interpretacion2[1]="Si el precio de cierre del " + str(dataframe2previous["fecha"][0]) + " fue de " + str(dataframe2previous["precios"][0]) + ", el precio de cierre del " + str(dataframe2["fecha"][0]) + " podria ser mayor a " + str(dataframe2previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion2[2]="Si el precio de cierre del " + str(dataframe2previous["fecha"][1]) + " fue de " + str(dataframe2previous["precios"][1]) + ", el precio de cierre del " + str(dataframe2["fecha"][1]) + " podria ser mayor a " + str(dataframe2previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion2[3]="Si el precio de cierre del " + str(dataframe2previous["fecha"][2]) + " fue de " + str(dataframe2previous["precios"][2]) + ", el precio de cierre del " + str(dataframe2["fecha"][2]) + " podria ser mayor a " + str(dataframe2previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion2[4]="Si el precio de cierre del " + str(dataframe2previous["fecha"][3]) + " fue de " + str(dataframe2previous["precios"][3]) + ", el precio de cierre del " + str(dataframe2["fecha"][3]) + " podria ser menor a " + str(dataframe2previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion2[5]="Si el precio de cierre del " + str(dataframe2previous["fecha"][4]) + " fue de " + str(dataframe2previous["precios"][4]) + ", el precio de cierre del " + str(dataframe2["fecha"][4]) + " podria ser menor a " + str(dataframe2previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion2[6]="Si el precio de cierre del " + str(dataframe2previous["fecha"][5]) + " fue de " + str(dataframe2previous["precios"][5]) + ", el precio de cierre del " + str(dataframe2["fecha"][5]) + " podria ser mayor a " + str(dataframe2previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion2[7]="Si el precio de cierre del " + str(dataframe2previous["fecha"][6]) + " fue de " + str(dataframe2previous["precios"][6]) + ", el precio de cierre del " + str(dataframe2["fecha"][6]) + " podria ser mayor a " + str(dataframe2previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13]) 
    interpretacion3={}
    interpretacion3[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 23-08-2018. Esto implicaria que:"
    interpretacion3[1]="Si el precio de cierre del " + str(dataframe3previous["fecha"][0]) + " fue de " + str(dataframe3previous["precios"][0]) + ", el precio de cierre del " + str(dataframe3["fecha"][0]) + " podria ser mayor a " + str(dataframe3previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion3[2]="Si el precio de cierre del " + str(dataframe3previous["fecha"][1]) + " fue de " + str(dataframe3previous["precios"][1]) + ", el precio de cierre del " + str(dataframe3["fecha"][1]) + " podria ser mayor a " + str(dataframe3previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion3[3]="Si el precio de cierre del " + str(dataframe3previous["fecha"][2]) + " fue de " + str(dataframe3previous["precios"][2]) + ", el precio de cierre del " + str(dataframe3["fecha"][2]) + " podria ser mayor a " + str(dataframe3previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion3[4]="Si el precio de cierre del " + str(dataframe3previous["fecha"][3]) + " fue de " + str(dataframe3previous["precios"][3]) + ", el precio de cierre del " + str(dataframe3["fecha"][3]) + " podria ser mayor a " + str(dataframe3previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion3[5]="Si el precio de cierre del " + str(dataframe3previous["fecha"][4]) + " fue de " + str(dataframe3previous["precios"][4]) + ", el precio de cierre del " + str(dataframe3["fecha"][4]) + " podria ser mayor a " + str(dataframe3previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion3[6]="Si el precio de cierre del " + str(dataframe3previous["fecha"][5]) + " fue de " + str(dataframe3previous["precios"][5]) + ", el precio de cierre del " + str(dataframe3["fecha"][5]) + " podria ser mayor a " + str(dataframe3previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion3[7]="Si el precio de cierre del " + str(dataframe3previous["fecha"][6]) + " fue de " + str(dataframe3previous["precios"][6]) + ", el precio de cierre del " + str(dataframe3["fecha"][6]) + " podria ser mayor a " + str(dataframe3previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13]) 
    interpretacion4={}
    interpretacion4[0]="El modelo sugiere que la tasa de cambio podria ser negativa el 30-08-2018, 31-08-2018 y positiva el 03-09-2018, 04-09-2018. Esto implicaria que:"
    interpretacion4[1]="Si el precio de cierre del " + str(dataframe4previous["fecha"][0]) + " fue de " + str(dataframe4previous["precios"][0]) + ", el precio de cierre del " + str(dataframe4["fecha"][0]) + " podria ser menor a " + str(dataframe4previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion4[2]="Si el precio de cierre del " + str(dataframe4previous["fecha"][1]) + " fue de " + str(dataframe4previous["precios"][1]) + ", el precio de cierre del " + str(dataframe4["fecha"][1]) + " podria ser menor a " + str(dataframe4previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion4[3]="Si el precio de cierre del " + str(dataframe4previous["fecha"][2]) + " fue de " + str(dataframe4previous["precios"][2]) + ", el precio de cierre del " + str(dataframe4["fecha"][2]) + " podria ser menor a " + str(dataframe4previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion4[4]="Si el precio de cierre del " + str(dataframe4previous["fecha"][3]) + " fue de " + str(dataframe4previous["precios"][3]) + ", el precio de cierre del " + str(dataframe4["fecha"][3]) + " podria ser menor a " + str(dataframe4previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion4[5]="Si el precio de cierre del " + str(dataframe4previous["fecha"][4]) + " fue de " + str(dataframe4previous["precios"][4]) + ", el precio de cierre del " + str(dataframe4["fecha"][4]) + " podria ser menor a " + str(dataframe4previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion4[6]="Si el precio de cierre del " + str(dataframe4previous["fecha"][5]) + " fue de " + str(dataframe4previous["precios"][5]) + ", el precio de cierre del " + str(dataframe4["fecha"][5]) + " podria ser mayor a " + str(dataframe4previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion4[7]="Si el precio de cierre del " + str(dataframe4previous["fecha"][6]) + " fue de " + str(dataframe4previous["precios"][6]) + ", el precio de cierre del " + str(dataframe4["fecha"][6]) + " podria ser mayor a " + str(dataframe4previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13]) 
    interpretacion5={}
    interpretacion5[0]="El modelo sugiere que la tasa de cambio podria ser  negativa a partir del 06-09-2018. Esto implicaria que:"
    interpretacion5[1]="Si el precio de cierre del " + str(dataframe5previous["fecha"][0]) + " fue de " + str(dataframe5previous["precios"][0]) + ", el precio de cierre del " + str(dataframe5["fecha"][0]) + " podria ser mayor a " + str(dataframe5previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion5[2]="Si el precio de cierre del " + str(dataframe5previous["fecha"][1]) + " fue de " + str(dataframe5previous["precios"][1]) + ", el precio de cierre del " + str(dataframe5["fecha"][1]) + " podria ser menor a " + str(dataframe5previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion5[3]="Si el precio de cierre del " + str(dataframe5previous["fecha"][2]) + " fue de " + str(dataframe5previous["precios"][2]) + ", el precio de cierre del " + str(dataframe5["fecha"][2]) + " podria ser menor a " + str(dataframe5previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion5[4]="Si el precio de cierre del " + str(dataframe5previous["fecha"][3]) + " fue de " + str(dataframe5previous["precios"][3]) + ", el precio de cierre del " + str(dataframe5["fecha"][3]) + " podria ser menor a " + str(dataframe5previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion5[5]="Si el precio de cierre del " + str(dataframe5previous["fecha"][4]) + " fue de " + str(dataframe5previous["precios"][4]) + ", el precio de cierre del " + str(dataframe5["fecha"][4]) + " podria ser menor a " + str(dataframe5previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion5[6]="Si el precio de cierre del " + str(dataframe5previous["fecha"][5]) + " fue de " + str(dataframe5previous["precios"][5]) + ", el precio de cierre del " + str(dataframe5["fecha"][5]) + " podria ser menor a " + str(dataframe5previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion5[7]="Si el precio de cierre del " + str(dataframe5previous["fecha"][6]) + " fue de " + str(dataframe5previous["precios"][6]) + ", el precio de cierre del " + str(dataframe5["fecha"][6]) + " podria ser menor a " + str(dataframe5previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13]) 
    interpretacion6={}
    interpretacion6[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 13-09-2018. Esto implicaria que:"
    interpretacion6[1]="Si el precio de cierre del " + str(dataframe6previous["fecha"][0]) + " fue de " + str(dataframe6previous["precios"][0]) + ", el precio de cierre del " + str(dataframe6["fecha"][0]) + " podria ser mayor a " + str(dataframe6previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion6[2]="Si el precio de cierre del " + str(dataframe6previous["fecha"][1]) + " fue de " + str(dataframe6previous["precios"][1]) + ", el precio de cierre del " + str(dataframe6["fecha"][1]) + " podria ser mayor a " + str(dataframe6previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion6[3]="Si el precio de cierre del " + str(dataframe6previous["fecha"][2]) + " fue de " + str(dataframe6previous["precios"][2]) + ", el precio de cierre del " + str(dataframe6["fecha"][2]) + " podria ser mayor a " + str(dataframe6previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion6[4]="Si el precio de cierre del " + str(dataframe6previous["fecha"][3]) + " fue de " + str(dataframe6previous["precios"][3]) + ", el precio de cierre del " + str(dataframe6["fecha"][3]) + " podria ser mayor a " + str(dataframe6previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion6[5]="Si el precio de cierre del " + str(dataframe6previous["fecha"][4]) + " fue de " + str(dataframe6previous["precios"][4]) + ", el precio de cierre del " + str(dataframe6["fecha"][4]) + " podria ser mayor a " + str(dataframe6previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion6[6]="Si el precio de cierre del " + str(dataframe6previous["fecha"][5]) + " fue de " + str(dataframe6previous["precios"][5]) + ", el precio de cierre del " + str(dataframe6["fecha"][5]) + " podria ser mayor a " + str(dataframe6previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion6[7]="Si el precio de cierre del " + str(dataframe6previous["fecha"][6]) + " fue de " + str(dataframe6previous["precios"][6]) + ", el precio de cierre del " + str(dataframe6["fecha"][6]) + " podria ser mayor a " + str(dataframe6previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13])      
    interpretacion7={}
    interpretacion7[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 20-09-2018. Esto implicaria que:"
    interpretacion7[1]="Si el precio de cierre del " + str(dataframe7previous["fecha"][0]) + " fue de " + str(dataframe7previous["precios"][0]) + ", el precio de cierre del " + str(dataframe7["fecha"][0]) + " podria ser mayor a " + str(dataframe7previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion7[2]="Si el precio de cierre del " + str(dataframe7previous["fecha"][1]) + " fue de " + str(dataframe7previous["precios"][1]) + ", el precio de cierre del " + str(dataframe7["fecha"][1]) + " podria ser mayor a " + str(dataframe7previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion7[3]="Si el precio de cierre del " + str(dataframe7previous["fecha"][2]) + " fue de " + str(dataframe7previous["precios"][2]) + ", el precio de cierre del " + str(dataframe7["fecha"][2]) + " podria ser mayor a " + str(dataframe7previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion7[4]="Si el precio de cierre del " + str(dataframe7previous["fecha"][3]) + " fue de " + str(dataframe7previous["precios"][3]) + ", el precio de cierre del " + str(dataframe7["fecha"][3]) + " podria ser mayor a " + str(dataframe7previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion7[5]="Si el precio de cierre del " + str(dataframe7previous["fecha"][4]) + " fue de " + str(dataframe7previous["precios"][4]) + ", el precio de cierre del " + str(dataframe7["fecha"][4]) + " podria ser mayor a " + str(dataframe7previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion7[6]="Si el precio de cierre del " + str(dataframe7previous["fecha"][5]) + " fue de " + str(dataframe7previous["precios"][5]) + ", el precio de cierre del " + str(dataframe7["fecha"][5]) + " podria ser mayor a " + str(dataframe7previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion7[7]="Si el precio de cierre del " + str(dataframe7previous["fecha"][6]) + " fue de " + str(dataframe7previous["precios"][6]) + ", el precio de cierre del " + str(dataframe7["fecha"][6]) + " podria ser mayor a " + str(dataframe7previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13])      
    
    interpretaciones=["dummy",interpretacion1,interpretacion2,interpretacion3,interpretacion4,interpretacion5,interpretacion6,interpretacion7]
    interpretacion=interpretaciones[number]	
    return render_template('line_chart.html', values_prediccion=prediccion,values_real=real,values_precios=precios, labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],interpretacion=interpretacion)
 
@app.route("/last_batch",methods=['POST','GET'])	
def last_batch():   
    fullPath='model/predicciones/'
    remainingPath='prediccionFinal.csv'
    df=pd.read_csv(fullPath+remainingPath,header=0)
    dataframeprevious=pd.read_csv("model/dataframeprevious.csv",header=0)
    prediccion=df['prediccion'] 
    real=df['real']
    fecha=df['fecha']  
    fecha=[str(i) for i in fecha]
    precios=df['precios']
    fechaInicio=fecha[0]
    fechaFin=fecha[6]
    interpretacion={}
    interpretacion[0]="El modelo sugiere que la tasa de cambio podria ser positiva a partir del 27-09-2018. Esto implicaria que:"
    interpretacion[1]="Si el precio de cierre del " + str(dataframeprevious["fecha"][0]) + " fue de " + str(dataframeprevious["precios"][0]) + ", el precio de cierre del " + "24-09-2018" + " podria ser mayor a " + str(dataframeprevious["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion[2]="Si el precio de cierre del " + str(dataframeprevious["fecha"][1]) + " fue de " + str(dataframeprevious["precios"][1]) + ", el precio de cierre del " + "25-09-2018" + " podria ser mayor a " + str(dataframeprevious["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion[3]="Si el precio de cierre del " + str(dataframeprevious["fecha"][2]) + " fue de " + str(dataframeprevious["precios"][2]) + ", el precio de cierre del " + "26-09-2018" + " podria ser mayor a " + str(dataframeprevious["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion[4]="Si el precio de cierre del " + str(dataframeprevious["fecha"][3]) + " fue de " + str(dataframeprevious["precios"][3]) + ", el precio de cierre del " + "27-09-2018" + " podria ser mayor a " + str(dataframeprevious["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion[5]="Si el precio de cierre del " + str(dataframeprevious["fecha"][4]) + " fue de " + str(dataframeprevious["precios"][4]) + ", el precio de cierre del " + "28-09-2018" + " podria ser mayor a " + str(dataframeprevious["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion[6]="Si el precio de cierre del " + str(dataframeprevious["fecha"][5]) + " fue de " + str(dataframeprevious["precios"][5]) + ", el precio de cierre del " + "01-10-2018" + " podria ser mayor a " + str(dataframeprevious["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion[7]="Si el precio de cierre del " + str(dataframeprevious["fecha"][6]) + " fue de " + str(dataframeprevious["precios"][6]) + ", el precio de cierre del " + "02-10-2018" + " podria ser mayor a " + str(dataframeprevious["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13])      
    x=pd.DataFrame({'fecha':["24-09-2018","25-09-2018","26-09-2018","27-09-2018","28-09-2018","01-10-2018","02-10-2018"],'precio de cierre':["","","","","","",""],'tasa de cambio':["","","","","","",""],'acierto del modelo':["","","","","","",""]})
    x=x[['fecha','precio de cierre','tasa de cambio','acierto del modelo']]
    x=x.iloc[3:,].reset_index(drop=True)
    x=x.iloc[::-1]
    return render_template('last_batch.html', values_prediccion=prediccion,values_real=real,values_precios=precios, labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],interpretacion=interpretacion)
   

   
if __name__ == "__main__":
    #app.run(debug=True,port=5000)
	app.run(debug=True)
print('You can check the website now!')