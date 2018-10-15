from flask import Flask
from flask import render_template,request
from datetime import time
   
import pandas as pd  
import numpy as np     
 
import matplotlib.pyplot as plt    

import math     
import datetime  

import glob
		   
app = Flask(__name__)   

def predicted_prices(predicted_rates,previous_real_prices):
    predicted_prices=[]
    for i in range(len(predicted_rates)):
        predicted_price=previous_real_prices[i]+(predicted_rates[i]*previous_real_prices[i])/100        	 
        predicted_prices.append(predicted_price)
    return predicted_prices
	
	            
def RSME(lista1,lista2):
    lista=[]
    for i in range(len(lista1)):
        square=(lista1[i]-lista2[i])*(lista1[i]-lista2[i])
        lista.append(square)
    rsme=sum(lista)/len(lista)
    return math.sqrt(rsme)  
		
@app.route("/")  
def main():
    return render_template('main.html')

@app.route("/line_chart",methods=['POST','GET']) 
def line_chart():  
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/*.csv'))]  
    fulldataframes=[pd.concat([dataframesprevious[i],dataframes[i]]).reset_index(drop=True) for i in range(len(dataframes))]  	
    price=prices[number]	
    fulldataframe=fulldataframes[number]	
    real=fulldataframe['tasa']         
    precios=fulldataframe['precios']
    #build predicted prices
    previous_real_prices_first_half=price['precios'].tolist()[0:7]
    predicted_rates_first_half=prediccion.tolist()[0:7]	
    previous_real_prices_second_half=price['precios'].tolist()[7:]
    predicted_rates_second_half=prediccion.tolist()[7:]		
    precios_prediccion=predicted_prices(predicted_rates_first_half,previous_real_prices_first_half)+predicted_prices(predicted_rates_second_half,previous_real_prices_second_half)	
    #
    x=dataframes[number]
    x['pronóstico tasa']=prediccion.tolist()[7:]	
    x['pronóstico precios']=precios_prediccion[7:]
    x=x[['fecha','precios','pronóstico precios','tasa','pronóstico tasa']]		
    x=x.reset_index(drop=True)		
    error_precios=RSME(precios[0:7],precios_prediccion[0:7])	
    return render_template('line_chart.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)
 
@app.route("/last_batch",methods=['POST','GET'])	
def last_batch():   
    df=pd.read_csv('model/predicciones/prediccion0.csv',header=0)
    prediccion=df['prediccion']
    dataframeprevious=pd.read_csv("model/dataframesprevious/dataframeprevious0.csv",header=0)
    dataframe=pd.read_csv("model/dataframes/dataframe0.csv",header=0)	
    fulldataframe=pd.concat([dataframeprevious,dataframe]).reset_index(drop=True)	
    price=pd.read_csv("model/precios/precios0.csv",header=0)	
    real=fulldataframe['tasa']
    fecha=df['fecha'] 
    fecha=[str(i) for i in fecha]
    precios=fulldataframe['precios']
    #build predicted prices
    previous_real_prices_first_half=price['precios'].tolist()[0:7]
    predicted_rates_first_half=prediccion.tolist()[0:7]	
    previous_real_prices_second_half=price['precios'].tolist()[7:]
    predicted_rates_second_half=prediccion.tolist()[7:]		
    precios_prediccion=predicted_prices(predicted_rates_first_half,previous_real_prices_first_half)+predicted_prices(predicted_rates_second_half,previous_real_prices_second_half)	
    #
    fechaInicio=fecha[0]
    fechaFin=fecha[6]
    x=dataframe
    x['pronóstico tasa']=prediccion.tolist()[7:]	
    x['pronóstico precios']=precios_prediccion[7:]
    x=x[['fecha','precios','pronóstico precios','tasa','pronóstico tasa']]
    x=x.reset_index(drop=True)	
    error_precios=RSME(precios[0:7],precios_prediccion[0:7])
    return render_template('last_batch.html', values_prediccion=prediccion,values_real=real,values_precios=precios,values_precios_prediccion=precios_prediccion, labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],precios_prediccion=precios_prediccion,error_precios=error_precios)
   

   
if __name__ == "__main__":
    #app.run(debug=True,port=5000)
	app.run(debug=True)
print('You can check the website now!')