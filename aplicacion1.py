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
def home():
    return render_template('home.html')

@app.route("/periodos",methods=['POST','GET'])  
def periodos():
    nombreEmisora=request.form.get('emisora',type=str)
    if nombreEmisora=="NAFTRAC":
        emisoraHTML="periodos"+nombreEmisora+".HTML"
    else:
        emisoraHTML="periodos"+nombreEmisora+".html"	
    return render_template(emisoraHTML)	
	
@app.route("/pronosticoAMXL",methods=['POST','GET']) 
def pronosticoAMXL():  
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/americamovil/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/americamovil/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/americamovil/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/americamovil/*.csv'))]  
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
    return render_template('pronosticoAMXL.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)

@app.route("/pronosticoNAFTRAC",methods=['POST','GET']) 
def pronosticoNAFTRAC():   
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/naftrac/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/naftrac/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/naftrac/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/naftrac/*.csv'))]  
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
    return render_template('pronosticoNAFTRAC.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)
 
@app.route("/pronosticoLALA",methods=['POST','GET']) 
def pronosticoLALA():   
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/lala/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/lala/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/lala/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/lala/*.csv'))]  
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
    return render_template('pronosticoLALA.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)
 
@app.route("/pronosticoLACOMUBC",methods=['POST','GET']) 
def pronosticoLACOMUBC():   
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/lacomer/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/lacomer/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/lacomer/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/lacomer/*.csv'))]  
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
    return render_template('pronosticoLACOMUBC.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)
 
@app.route("/pronosticoLIVEPOLC",methods=['POST','GET']) 
def pronosticoLIVEPOLC():   
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/liverpool/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/liverpool/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/liverpool/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/liverpool/*.csv'))]  
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
    return render_template('pronosticoLIVEPOLC.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)

@app.route("/pronosticoALSEA",methods=['POST','GET']) 
def pronosticoALSEA():   
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/alsea/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/alsea/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/alsea/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/alsea/*.csv'))]  
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
    return render_template('pronosticoALSEA.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)
 
@app.route("/pronosticoGFNORTEO",methods=['POST','GET']) 
def pronosticoGFNORTEO():   
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/banorte/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/banorte/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/banorte/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/banorte/*.csv'))]  
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
    return render_template('pronosticoGFNORTEO.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)
 
@app.route("/pronosticoAXTELCPO",methods=['POST','GET']) 
def pronosticoAXTELCPO():   
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/axtel/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/axtel/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/axtel/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/axtel/*.csv'))]  
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
    return render_template('pronosticoAXTELCPO.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)
 
 
   
if __name__ == "__home__":
    #app.run(debug=True,port=5000)
	app.run(debug=True)
print('You can check the website now!')