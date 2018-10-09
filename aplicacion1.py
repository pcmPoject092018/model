from flask import Flask
from flask import render_template,request
from datetime import time
   
import pandas as pd  
import numpy as np     
 
import matplotlib.pyplot as plt    

import math     
import datetime  
 
		   
app = Flask(__name__)   

def predicted_prices(predicted_rates,previous_real_prices):
    predicted_prices=[]
    for i in range(len(predicted_rates)):
        predicted_price=previous_real_prices[i]+(predicted_rates[i]*previous_real_prices[i])/100        	 
        predicted_prices.append(predicted_price)
    return predicted_prices
		
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
    fecha=df['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframe1=pd.read_csv("model/dataframe1.csv",header=0)
    dataframe2=pd.read_csv("model/dataframe2.csv",header=0)
    dataframe3=pd.read_csv("model/dataframe3.csv",header=0)
    dataframe4=pd.read_csv("model/dataframe4.csv",header=0)
    dataframe5=pd.read_csv("model/dataframe5.csv",header=0)
    dataframe6=pd.read_csv("model/dataframe6.csv",header=0)
    dataframe7=pd.read_csv("model/dataframe7.csv",header=0)
    dataframe8=pd.read_csv("model/dataframe8.csv",header=0)
    dataframe9=pd.read_csv("model/dataframe9.csv",header=0)
    dataframe10=pd.read_csv("model/dataframe10.csv",header=0)
    dataframe1previous=pd.read_csv("model/dataframe1previous.csv",header=0)
    dataframe2previous=pd.read_csv("model/dataframe2previous.csv",header=0)
    dataframe3previous=pd.read_csv("model/dataframe3previous.csv",header=0)
    dataframe4previous=pd.read_csv("model/dataframe4previous.csv",header=0)
    dataframe5previous=pd.read_csv("model/dataframe5previous.csv",header=0)
    dataframe6previous=pd.read_csv("model/dataframe6previous.csv",header=0)
    dataframe7previous=pd.read_csv("model/dataframe7previous.csv",header=0)
    dataframe8previous=pd.read_csv("model/dataframe8previous.csv",header=0)
    dataframe9previous=pd.read_csv("model/dataframe9previous.csv",header=0)	
    dataframe10previous=pd.read_csv("model/dataframe10previous.csv",header=0)	
    fulldataframe1=pd.concat([dataframe1previous,dataframe1]).reset_index(drop=True)	
    fulldataframe2=pd.concat([dataframe2previous,dataframe2]).reset_index(drop=True)			
    fulldataframe3=pd.concat([dataframe3previous,dataframe3]).reset_index(drop=True)		
    fulldataframe4=pd.concat([dataframe4previous,dataframe4]).reset_index(drop=True)		
    fulldataframe5=pd.concat([dataframe5previous,dataframe5]).reset_index(drop=True)		
    fulldataframe6=pd.concat([dataframe6previous,dataframe6]).reset_index(drop=True)		
    fulldataframe7=pd.concat([dataframe7previous,dataframe7]).reset_index(drop=True)		
    fulldataframe8=pd.concat([dataframe8previous,dataframe8]).reset_index(drop=True)		
    fulldataframe9=pd.concat([dataframe9previous,dataframe9]).reset_index(drop=True)		
    fulldataframe10=pd.concat([dataframe10previous,dataframe10]).reset_index(drop=True)		
    dataframe1["acierto del modelo"]=["","","","si","si","no","si"]
    dataframe2["acierto del modelo"]=["","","","si","si","si","si"]	
    dataframe3["acierto del modelo"]=["","","","si","si","si","si"]	
    dataframe4["acierto del modelo"]=["","","","si","si","si","no"]	
    dataframe5["acierto del modelo"]=["","","","si","si","si","si"]	
    dataframe6["acierto del modelo"]=["","","","si","si","si","no"]
    dataframe7["acierto del modelo"]=["","","","si","no","no","no"]	
    dataframe8["acierto del modelo"]=["","","","no","no","no","no"]
    dataframe9["acierto del modelo"]=["","","","si","si","si",""]	
    dataframe10["acierto del modelo"]=["","","","","","",""]		
    dataframes=["dummy",dataframe1,dataframe2,dataframe3,dataframe4,dataframe5,dataframe6,dataframe7,dataframe8,dataframe9,dataframe10]
    fulldataframes=["dummy",fulldataframe1,fulldataframe2,fulldataframe3,fulldataframe4,fulldataframe5,fulldataframe6,fulldataframe7,fulldataframe8,fulldataframe9,fulldataframe10]	
    interpretacion1={}
    interpretacion1[0]="El modelo sugiere que la tasa de cambio podría ser negativa a partir del 09-08-2018 excepto el 14-08-2018. Esto implicaría que:"
    interpretacion1[1]="Si el precio de cierre del " + str(dataframe1previous["fecha"][0]) + " fue de " + str(dataframe1previous["precios"][0]) + ", el precio de cierre del " + str(dataframe1["fecha"][0]) + " podría ser mayor a " + str(dataframe1previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion1[2]="Si el precio de cierre del " + str(dataframe1previous["fecha"][1]) + " fue de " + str(dataframe1previous["precios"][1]) + ", el precio de cierre del " + str(dataframe1["fecha"][1]) + " podría ser mayor a " + str(dataframe1previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion1[3]="Si el precio de cierre del " + str(dataframe1previous["fecha"][2]) + " fue de " + str(dataframe1previous["precios"][2]) + ", el precio de cierre del " + str(dataframe1["fecha"][2]) + " podría ser menor a " + str(dataframe1previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion1[4]="Si el precio de cierre del " + str(dataframe1previous["fecha"][3]) + " fue de " + str(dataframe1previous["precios"][3]) + ", el precio de cierre del " + str(dataframe1["fecha"][3]) + " podría ser menor a " + str(dataframe1previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion1[5]="Si el precio de cierre del " + str(dataframe1previous["fecha"][4]) + " fue de " + str(dataframe1previous["precios"][4]) + ", el precio de cierre del " + str(dataframe1["fecha"][4]) + " podría ser menor a " + str(dataframe1previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion1[6]="Si el precio de cierre del " + str(dataframe1previous["fecha"][5]) + " fue de " + str(dataframe1previous["precios"][5]) + ", el precio de cierre del " + str(dataframe1["fecha"][5]) + " podría ser menor a " + str(dataframe1previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion1[7]="Si el precio de cierre del " + str(dataframe1previous["fecha"][6]) + " fue de " + str(dataframe1previous["precios"][6]) + ", el precio de cierre del " + str(dataframe1["fecha"][6]) + " podría ser mayor a " + str(dataframe1previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13]) 
    interpretacion2={}
    interpretacion2[0]="El modelo sugiere que la tasa de cambio podría ser negativa el 16-08-2018, 17-08-2918 y positiva el 20-08-2018, 21-08-2018. Esto implicaría que:"
    interpretacion2[1]="Si el precio de cierre del " + str(dataframe2previous["fecha"][0]) + " fue de " + str(dataframe2previous["precios"][0]) + ", el precio de cierre del " + str(dataframe2["fecha"][0]) + " podría ser mayor a " + str(dataframe2previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion2[2]="Si el precio de cierre del " + str(dataframe2previous["fecha"][1]) + " fue de " + str(dataframe2previous["precios"][1]) + ", el precio de cierre del " + str(dataframe2["fecha"][1]) + " podría ser mayor a " + str(dataframe2previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion2[3]="Si el precio de cierre del " + str(dataframe2previous["fecha"][2]) + " fue de " + str(dataframe2previous["precios"][2]) + ", el precio de cierre del " + str(dataframe2["fecha"][2]) + " podría ser mayor a " + str(dataframe2previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion2[4]="Si el precio de cierre del " + str(dataframe2previous["fecha"][3]) + " fue de " + str(dataframe2previous["precios"][3]) + ", el precio de cierre del " + str(dataframe2["fecha"][3]) + " podría ser menor a " + str(dataframe2previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion2[5]="Si el precio de cierre del " + str(dataframe2previous["fecha"][4]) + " fue de " + str(dataframe2previous["precios"][4]) + ", el precio de cierre del " + str(dataframe2["fecha"][4]) + " podría ser menor a " + str(dataframe2previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion2[6]="Si el precio de cierre del " + str(dataframe2previous["fecha"][5]) + " fue de " + str(dataframe2previous["precios"][5]) + ", el precio de cierre del " + str(dataframe2["fecha"][5]) + " podría ser mayor a " + str(dataframe2previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion2[7]="Si el precio de cierre del " + str(dataframe2previous["fecha"][6]) + " fue de " + str(dataframe2previous["precios"][6]) + ", el precio de cierre del " + str(dataframe2["fecha"][6]) + " podría ser mayor a " + str(dataframe2previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13]) 
    interpretacion3={}
    interpretacion3[0]="El modelo sugiere que la tasa de cambio podría ser positiva a partir del 23-08-2018. Esto implicaría que:"
    interpretacion3[1]="Si el precio de cierre del " + str(dataframe3previous["fecha"][0]) + " fue de " + str(dataframe3previous["precios"][0]) + ", el precio de cierre del " + str(dataframe3["fecha"][0]) + " podría ser mayor a " + str(dataframe3previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion3[2]="Si el precio de cierre del " + str(dataframe3previous["fecha"][1]) + " fue de " + str(dataframe3previous["precios"][1]) + ", el precio de cierre del " + str(dataframe3["fecha"][1]) + " podría ser mayor a " + str(dataframe3previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion3[3]="Si el precio de cierre del " + str(dataframe3previous["fecha"][2]) + " fue de " + str(dataframe3previous["precios"][2]) + ", el precio de cierre del " + str(dataframe3["fecha"][2]) + " podría ser mayor a " + str(dataframe3previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion3[4]="Si el precio de cierre del " + str(dataframe3previous["fecha"][3]) + " fue de " + str(dataframe3previous["precios"][3]) + ", el precio de cierre del " + str(dataframe3["fecha"][3]) + " podría ser mayor a " + str(dataframe3previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion3[5]="Si el precio de cierre del " + str(dataframe3previous["fecha"][4]) + " fue de " + str(dataframe3previous["precios"][4]) + ", el precio de cierre del " + str(dataframe3["fecha"][4]) + " podría ser mayor a " + str(dataframe3previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion3[6]="Si el precio de cierre del " + str(dataframe3previous["fecha"][5]) + " fue de " + str(dataframe3previous["precios"][5]) + ", el precio de cierre del " + str(dataframe3["fecha"][5]) + " podría ser mayor a " + str(dataframe3previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion3[7]="Si el precio de cierre del " + str(dataframe3previous["fecha"][6]) + " fue de " + str(dataframe3previous["precios"][6]) + ", el precio de cierre del " + str(dataframe3["fecha"][6]) + " podría ser mayor a " + str(dataframe3previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13]) 
    interpretacion4={}
    interpretacion4[0]="El modelo sugiere que la tasa de cambio podría ser negativa el 30-08-2018, 31-08-2018 y positiva el 03-09-2018, 04-09-2018. Esto implicaría que:"
    interpretacion4[1]="Si el precio de cierre del " + str(dataframe4previous["fecha"][0]) + " fue de " + str(dataframe4previous["precios"][0]) + ", el precio de cierre del " + str(dataframe4["fecha"][0]) + " podría ser menor a " + str(dataframe4previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion4[2]="Si el precio de cierre del " + str(dataframe4previous["fecha"][1]) + " fue de " + str(dataframe4previous["precios"][1]) + ", el precio de cierre del " + str(dataframe4["fecha"][1]) + " podría ser menor a " + str(dataframe4previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion4[3]="Si el precio de cierre del " + str(dataframe4previous["fecha"][2]) + " fue de " + str(dataframe4previous["precios"][2]) + ", el precio de cierre del " + str(dataframe4["fecha"][2]) + " podría ser menor a " + str(dataframe4previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion4[4]="Si el precio de cierre del " + str(dataframe4previous["fecha"][3]) + " fue de " + str(dataframe4previous["precios"][3]) + ", el precio de cierre del " + str(dataframe4["fecha"][3]) + " podría ser menor a " + str(dataframe4previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion4[5]="Si el precio de cierre del " + str(dataframe4previous["fecha"][4]) + " fue de " + str(dataframe4previous["precios"][4]) + ", el precio de cierre del " + str(dataframe4["fecha"][4]) + " podría ser menor a " + str(dataframe4previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion4[6]="Si el precio de cierre del " + str(dataframe4previous["fecha"][5]) + " fue de " + str(dataframe4previous["precios"][5]) + ", el precio de cierre del " + str(dataframe4["fecha"][5]) + " podría ser mayor a " + str(dataframe4previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion4[7]="Si el precio de cierre del " + str(dataframe4previous["fecha"][6]) + " fue de " + str(dataframe4previous["precios"][6]) + ", el precio de cierre del " + str(dataframe4["fecha"][6]) + " podría ser mayor a " + str(dataframe4previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13]) 
    interpretacion5={}
    interpretacion5[0]="El modelo sugiere que la tasa de cambio podría ser  negativa a partir del 06-09-2018. Esto implicaría que:"
    interpretacion5[1]="Si el precio de cierre del " + str(dataframe5previous["fecha"][0]) + " fue de " + str(dataframe5previous["precios"][0]) + ", el precio de cierre del " + str(dataframe5["fecha"][0]) + " podría ser mayor a " + str(dataframe5previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion5[2]="Si el precio de cierre del " + str(dataframe5previous["fecha"][1]) + " fue de " + str(dataframe5previous["precios"][1]) + ", el precio de cierre del " + str(dataframe5["fecha"][1]) + " podría ser menor a " + str(dataframe5previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion5[3]="Si el precio de cierre del " + str(dataframe5previous["fecha"][2]) + " fue de " + str(dataframe5previous["precios"][2]) + ", el precio de cierre del " + str(dataframe5["fecha"][2]) + " podría ser menor a " + str(dataframe5previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion5[4]="Si el precio de cierre del " + str(dataframe5previous["fecha"][3]) + " fue de " + str(dataframe5previous["precios"][3]) + ", el precio de cierre del " + str(dataframe5["fecha"][3]) + " podría ser menor a " + str(dataframe5previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion5[5]="Si el precio de cierre del " + str(dataframe5previous["fecha"][4]) + " fue de " + str(dataframe5previous["precios"][4]) + ", el precio de cierre del " + str(dataframe5["fecha"][4]) + " podría ser menor a " + str(dataframe5previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion5[6]="Si el precio de cierre del " + str(dataframe5previous["fecha"][5]) + " fue de " + str(dataframe5previous["precios"][5]) + ", el precio de cierre del " + str(dataframe5["fecha"][5]) + " podría ser menor a " + str(dataframe5previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion5[7]="Si el precio de cierre del " + str(dataframe5previous["fecha"][6]) + " fue de " + str(dataframe5previous["precios"][6]) + ", el precio de cierre del " + str(dataframe5["fecha"][6]) + " podría ser menor a " + str(dataframe5previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13]) 
    interpretacion6={}
    interpretacion6[0]="El modelo sugiere que la tasa de cambio podría ser positiva a partir del 13-09-2018. Esto implicaría que:"
    interpretacion6[1]="Si el precio de cierre del " + str(dataframe6previous["fecha"][0]) + " fue de " + str(dataframe6previous["precios"][0]) + ", el precio de cierre del " + str(dataframe6["fecha"][0]) + " podría ser mayor a " + str(dataframe6previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion6[2]="Si el precio de cierre del " + str(dataframe6previous["fecha"][1]) + " fue de " + str(dataframe6previous["precios"][1]) + ", el precio de cierre del " + str(dataframe6["fecha"][1]) + " podría ser mayor a " + str(dataframe6previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion6[3]="Si el precio de cierre del " + str(dataframe6previous["fecha"][2]) + " fue de " + str(dataframe6previous["precios"][2]) + ", el precio de cierre del " + str(dataframe6["fecha"][2]) + " podría ser mayor a " + str(dataframe6previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion6[4]="Si el precio de cierre del " + str(dataframe6previous["fecha"][3]) + " fue de " + str(dataframe6previous["precios"][3]) + ", el precio de cierre del " + str(dataframe6["fecha"][3]) + " podría ser mayor a " + str(dataframe6previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion6[5]="Si el precio de cierre del " + str(dataframe6previous["fecha"][4]) + " fue de " + str(dataframe6previous["precios"][4]) + ", el precio de cierre del " + str(dataframe6["fecha"][4]) + " podría ser mayor a " + str(dataframe6previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion6[6]="Si el precio de cierre del " + str(dataframe6previous["fecha"][5]) + " fue de " + str(dataframe6previous["precios"][5]) + ", el precio de cierre del " + str(dataframe6["fecha"][5]) + " podría ser mayor a " + str(dataframe6previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion6[7]="Si el precio de cierre del " + str(dataframe6previous["fecha"][6]) + " fue de " + str(dataframe6previous["precios"][6]) + ", el precio de cierre del " + str(dataframe6["fecha"][6]) + " podría ser mayor a " + str(dataframe6previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13])      
    interpretacion7={}
    interpretacion7[0]="El modelo sugiere que la tasa de cambio podría ser positiva a partir del 20-09-2018. Esto implicaría que:"
    interpretacion7[1]="Si el precio de cierre del " + str(dataframe7previous["fecha"][0]) + " fue de " + str(dataframe7previous["precios"][0]) + ", el precio de cierre del " + str(dataframe7["fecha"][0]) + " podría ser mayor a " + str(dataframe7previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion7[2]="Si el precio de cierre del " + str(dataframe7previous["fecha"][1]) + " fue de " + str(dataframe7previous["precios"][1]) + ", el precio de cierre del " + str(dataframe7["fecha"][1]) + " podría ser mayor a " + str(dataframe7previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion7[3]="Si el precio de cierre del " + str(dataframe7previous["fecha"][2]) + " fue de " + str(dataframe7previous["precios"][2]) + ", el precio de cierre del " + str(dataframe7["fecha"][2]) + " podría ser mayor a " + str(dataframe7previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion7[4]="Si el precio de cierre del " + str(dataframe7previous["fecha"][3]) + " fue de " + str(dataframe7previous["precios"][3]) + ", el precio de cierre del " + str(dataframe7["fecha"][3]) + " podría ser mayor a " + str(dataframe7previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion7[5]="Si el precio de cierre del " + str(dataframe7previous["fecha"][4]) + " fue de " + str(dataframe7previous["precios"][4]) + ", el precio de cierre del " + str(dataframe7["fecha"][4]) + " podría ser mayor a " + str(dataframe7previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion7[6]="Si el precio de cierre del " + str(dataframe7previous["fecha"][5]) + " fue de " + str(dataframe7previous["precios"][5]) + ", el precio de cierre del " + str(dataframe7["fecha"][5]) + " podría ser mayor a " + str(dataframe7previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion7[7]="Si el precio de cierre del " + str(dataframe7previous["fecha"][6]) + " fue de " + str(dataframe7previous["precios"][6]) + ", el precio de cierre del " + str(dataframe7["fecha"][6]) + " podría ser mayor a " + str(dataframe7previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13])      
    interpretacion8={}
    interpretacion8[0]="El modelo sugiere que la tasa de cambio podría ser positiva a partir del 27-09-2018. Esto implicaría que:"
    interpretacion8[1]="Si el precio de cierre del " + str(dataframe8previous["fecha"][0]) + " fue de " + str(dataframe8previous["precios"][0]) + ", el precio de cierre del " + str(dataframe8["fecha"][0]) + " podría ser mayor a " + str(dataframe8previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion8[2]="Si el precio de cierre del " + str(dataframe8previous["fecha"][1]) + " fue de " + str(dataframe8previous["precios"][1]) + ", el precio de cierre del " + str(dataframe8["fecha"][1]) + " podría ser mayor a " + str(dataframe8previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion8[3]="Si el precio de cierre del " + str(dataframe8previous["fecha"][2]) + " fue de " + str(dataframe8previous["precios"][2]) + ", el precio de cierre del " + str(dataframe8["fecha"][2]) + " podría ser mayor a " + str(dataframe8previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion8[4]="Si el precio de cierre del " + str(dataframe8previous["fecha"][3]) + " fue de " + str(dataframe8previous["precios"][3]) + ", el precio de cierre del " + str(dataframe8["fecha"][3]) + " podría ser mayor a " + str(dataframe8previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion8[5]="Si el precio de cierre del " + str(dataframe8previous["fecha"][4]) + " fue de " + str(dataframe8previous["precios"][4]) + ", el precio de cierre del " + str(dataframe8["fecha"][4]) + " podría ser mayor a " + str(dataframe8previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion8[6]="Si el precio de cierre del " + str(dataframe8previous["fecha"][5]) + " fue de " + str(dataframe8previous["precios"][5]) + ", el precio de cierre del " + str(dataframe8["fecha"][5]) + " podría ser mayor a " + str(dataframe8previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion8[7]="Si el precio de cierre del " + str(dataframe8previous["fecha"][6]) + " fue de " + str(dataframe8previous["precios"][6]) + ", el precio de cierre del " + str(dataframe8["fecha"][6]) + " podría ser mayor a " + str(dataframe8previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13])      
    interpretacion9={}
    interpretacion9[0]="El modelo sugiere que la tasa de cambio podría ser negativa a partir 04-10-2018 excepto el 09-10-2018. Esto implicaría que:"
    interpretacion9[1]="Si el precio de cierre del " + str(dataframe9previous["fecha"][0]) + " fue de " + str(dataframe9previous["precios"][0]) + ", el precio de cierre del " + str(dataframe9["fecha"][0]) + " podría ser ... a " + str(dataframe9previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion9[2]="Si el precio de cierre del " + str(dataframe9previous["fecha"][1]) + " fue de " + str(dataframe9previous["precios"][1]) + ", el precio de cierre del " + str(dataframe9["fecha"][1]) + " podría ser ... a " + str(dataframe9previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion9[3]="Si el precio de cierre del " + str(dataframe9previous["fecha"][2]) + " fue de " + str(dataframe9previous["precios"][2]) + ", el precio de cierre del " + str(dataframe9["fecha"][2]) + " podría ser ... a " + str(dataframe9previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion9[4]="Si el precio de cierre del " + str(dataframe9previous["fecha"][3]) + " fue de " + str(dataframe9previous["precios"][3]) + ", el precio de cierre del " + str(dataframe9["fecha"][3]) + " podría ser menor a " + str(dataframe9previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion9[5]="Si el precio de cierre del " + str(dataframe9previous["fecha"][4]) + " fue de " + str(dataframe9previous["precios"][4]) + ", el precio de cierre del " + str(dataframe9["fecha"][4]) + " podría ser menor a " + str(dataframe9previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion9[6]="Si el precio de cierre del " + str(dataframe9previous["fecha"][5]) + " fue de " + str(dataframe9previous["precios"][5]) + ", el precio de cierre del " + str(dataframe9["fecha"][5]) + " podría ser menor a " + str(dataframe9previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion9[7]="Si el precio de cierre del " + str(dataframe9previous["fecha"][6]) + " fue de " + str(dataframe9previous["precios"][6]) + ", el precio de cierre del " + str(dataframe9["fecha"][6]) + " podría ser mayor a " + str(dataframe9previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13])    
    interpretacion10={}
    interpretacion10[0]="El modelo sugiere que la tasa de cambio podría ser positiva el 09-10-2018 y negativa a partir del 10-10-2018. Esto implicaría que:"
    interpretacion10[1]="Si el precio de cierre del " + str(dataframe10previous["fecha"][0]) + " fue de " + str(dataframe10previous["precios"][0]) + ", el precio de cierre del " + str(dataframe10["fecha"][0]) + " podría ser ... a " + str(dataframe10previous["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion10[2]="Si el precio de cierre del " + str(dataframe10previous["fecha"][1]) + " fue de " + str(dataframe10previous["precios"][1]) + ", el precio de cierre del " + str(dataframe10["fecha"][1]) + " podría ser ... a " + str(dataframe10previous["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion10[3]="Si el precio de cierre del " + str(dataframe10previous["fecha"][2]) + " fue de " + str(dataframe10previous["precios"][2]) + ", el precio de cierre del " + str(dataframe10["fecha"][2]) + " podría ser ... a " + str(dataframe10previous["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion10[4]="Si el precio de cierre del " + str(dataframe10previous["fecha"][3]) + " fue de " + str(dataframe10previous["precios"][3]) + ", el precio de cierre del " + str(dataframe10["fecha"][3]) + " podría ser mayor a " + str(dataframe10previous["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion10[5]="Si el precio de cierre del " + str(dataframe10previous["fecha"][4]) + " fue de " + str(dataframe10previous["precios"][4]) + ", el precio de cierre del " + str(dataframe10["fecha"][4]) + " podría ser menor a " + str(dataframe10previous["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion10[6]="Si el precio de cierre del " + str(dataframe10previous["fecha"][5]) + " fue de " + str(dataframe10previous["precios"][5]) + ", el precio de cierre del " + str(dataframe10["fecha"][5]) + " podría ser menor a " + str(dataframe10previous["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion10[7]="Si el precio de cierre del " + str(dataframe10previous["fecha"][6]) + " fue de " + str(dataframe10previous["precios"][6]) + ", el precio de cierre del " + str(dataframe10["fecha"][6]) + " podría ser menor a " + str(dataframe10previous["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13])      
    interpretaciones=["dummy",interpretacion1,interpretacion2,interpretacion3,interpretacion4,interpretacion5,interpretacion6,interpretacion7,interpretacion8,interpretacion9,interpretacion10]
    interpretacion=interpretaciones[number]
    fulldataframe=fulldataframes[number]	
    real=fulldataframe['tasa']         
    precios=fulldataframe['precios']
    precios_prediccion=["","","","","","",""]
    x=dataframes[number]
    x['pronóstico tasa']=prediccion.tolist()[7:]	
    x['pronóstico precios']=precios_prediccion
    x=x[['fecha','precios','pronóstico precios','tasa','pronóstico tasa','acierto del modelo']]		
    x=x.reset_index(drop=True)	
    x=x.iloc[3:,] #ultimos 4 pronosticos
    x=x.iloc[::-1]		
    return render_template('line_chart.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],interpretacion=interpretacion)
 
@app.route("/last_batch",methods=['POST','GET'])	
def last_batch():   
    fullPath='model/predicciones/'
    remainingPath='prediccionFinal.csv'
    df=pd.read_csv(fullPath+remainingPath,header=0)
    dataframeprevious=pd.read_csv("model/dataframeprevious.csv",header=0)
    dataframe=pd.read_csv("model/dataframe.csv",header=0)	
    fulldataframe=pd.concat([dataframeprevious,dataframe]).reset_index(drop=True)	
    prediccion=df['prediccion'] 
    real=fulldataframe['tasa']
    fecha=df['fecha']  
    fecha=[str(i) for i in fecha]
    precios=fulldataframe['precios']
    fechaInicio=fecha[0]
    fechaFin=fecha[6]
    interpretacion={}
    interpretacion[0]="El modelo sugiere que la tasa de cambio podría ser positiva a partir del 11-10-2018 Esto implicaría que:"
    interpretacion[1]="Si el precio de cierre del " + str(dataframeprevious["fecha"][0]) + " fue de " + str(dataframeprevious["precios"][0]) + ", el precio de cierre del " + str(dataframe["fecha"][0]) + " podría ser ... a " + str(dataframeprevious["precios"][0]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[7])
    interpretacion[2]="Si el precio de cierre del " + str(dataframeprevious["fecha"][1]) + " fue de " + str(dataframeprevious["precios"][1]) + ", el precio de cierre del " + str(dataframe["fecha"][1]) + " podría ser ... a " + str(dataframeprevious["precios"][1]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[8])
    interpretacion[3]="Si el precio de cierre del " + str(dataframeprevious["fecha"][2]) + " fue de " + str(dataframeprevious["precios"][2]) + ", el precio de cierre del " + str(dataframe["fecha"][2]) + " podría ser ... a " + str(dataframeprevious["precios"][2]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[9])
    interpretacion[4]="Si el precio de cierre del " + str(dataframeprevious["fecha"][3]) + " fue de " + str(dataframeprevious["precios"][3]) + ", el precio de cierre del " + str(dataframe["fecha"][3]) + " podría ser mayor a " + str(dataframeprevious["precios"][3]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[10])
    interpretacion[5]="Si el precio de cierre del " + str(dataframeprevious["fecha"][4]) + " fue de " + str(dataframeprevious["precios"][4]) + ", el precio de cierre del " + str(dataframe["fecha"][4]) + " podría ser mayor a " + str(dataframeprevious["precios"][4]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[11])
    interpretacion[6]="Si el precio de cierre del " + str(dataframeprevious["fecha"][5]) + " fue de " + str(dataframeprevious["precios"][5]) + ", el precio de cierre del " + str(dataframe["fecha"][5]) + " podría ser mayor a " + str(dataframeprevious["precios"][5]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[12])
    interpretacion[7]="Si el precio de cierre del " + str(dataframeprevious["fecha"][6]) + " fue de " + str(dataframeprevious["precios"][6]) + ", el precio de cierre del " + str(dataframe["fecha"][6]) + " podría ser mayor a " + str(dataframeprevious["precios"][6]) +" con una tasa de cambio posiblemente cercana a " + str(prediccion[13])      
    x=dataframe
    x['acierto del modelo']=["","","","","","",""]
    precios_prediccion=["","","","","","",""]	
    x['pronóstico tasa']=prediccion.tolist()[7:]	
    x['pronóstico precios']=precios_prediccion
    x=x[['fecha','precios','pronóstico precios','tasa','pronóstico tasa','acierto del modelo']]
    x=x.reset_index(drop=True)	
    x=x.iloc[3:,]
    x=x.iloc[::-1]
    return render_template('last_batch.html', values_prediccion=prediccion,values_real=real,values_precios=precios,values_precios_prediccion=precios_prediccion, labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],interpretacion=interpretacion)
   

   
if __name__ == "__main__":
    #app.run(debug=True,port=5000)
	app.run(debug=True)
print('You can check the website now!')