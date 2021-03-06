from flask import Flask
from flask import render_template,request
from datetime import time

from sklearn.linear_model import LogisticRegression   
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
 
@app.route("/pronosticoBIMBOA",methods=['POST','GET']) 
def pronosticoBIMBOA():   
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/bimbo/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/bimbo/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/bimbo/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/bimbo/*.csv'))]  
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
    return render_template('pronosticoBIMBOA.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)
 
@app.route("/pronosticoALPEKA",methods=['POST','GET']) 
def pronosticoALPEKA():   
    number = request.form.get('ejemplo',type=int)
    dfs=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/predicciones/alpek/*.csv'))]	
    prediccion=dfs[number]['prediccion']    
    fecha=dfs[number]['fecha'] 	      	       
    fechaInicio=fecha[0]  
    fechaFin=fecha[6]
    dataframes=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframes/alpek/*.csv'))]
    dataframesprevious=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/dataframesprevious/alpek/*.csv'))]	
    prices=[pd.read_csv(file,header=0) for file in sorted(glob.glob('model/precios/alpek/*.csv'))]  
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
    return render_template('pronosticoALPEKA.html', values_prediccion=prediccion,values_real=real,values_precios=precios, values_precios_prediccion=precios_prediccion,labels=fecha,fechaInicio=fechaInicio,fechaFin=fechaFin,tables=[x.to_html(classes='table')],error_precios=error_precios)
 
##################################################################################################################################

def buildFeatures(precios,fechas,nFeatures):
    moves={}
    for i in range(nFeatures,len(precios)):
        move=[]
        for j in reversed(range(1,nFeatures+1)):
            if precios[i-j]<=precios[i]:
                move.append(0)
            else:
                move.append(1)
        moves[fechas[i]]=move
    return moves  
	
def buildLabel(precios,fechas,nAhead,nFeatures):
    moveAhead={}
    for i in range(nFeatures,len(precios)-nAhead):
        if precios[i]<precios[i+nAhead]:
            moveAhead[fechas[i]]=1
        else:
            moveAhead[fechas[i]]=0
    return moveAhead 	

def data(lengthHistorico,emisora):
    pathData="model/data/"+emisora+".csv"
    amov=pd.read_csv(pathData,header=6,sep=",")[::-1].reset_index(drop=True) 
    initial=amov.shape[0]-lengthHistorico
    amov=amov.iloc[initial:,:].reset_index()
    precios=amov['PRECIO']
    fechas=amov['Date']
    return precios, fechas	
	
def Score(nFeatures,nAhead,lengthHistorico,emisora,trainSize,C,fit_intercept):
    precios, fechas=data(lengthHistorico,emisora)
    features=buildFeatures(precios,fechas,nFeatures)
    label=buildLabel(precios,fechas,nAhead,nFeatures)
    labels=list(label.values())
    observations=list(features.values())[0:len(labels)]
    dates=list(label.keys())
    df=pd.concat([pd.DataFrame(observations),pd.DataFrame(labels),pd.DataFrame(dates)],axis=1)
    df.columns=["day"+str(i) for i in range(1,nFeatures+1)]+["target","fecha"]
    trainLength=round(df.shape[0]*trainSize)
    train=df.iloc[0:trainLength,0:nFeatures+1]
    test=df.iloc[trainLength:,0:nFeatures+1]
    lr=LogisticRegression(C=C,fit_intercept=fit_intercept)
    score=lr.fit(train.iloc[:,0:nFeatures],train["target"]).score(test.iloc[:,0:nFeatures],test["target"])
    return score

def gridSearch(nFeaturesList,nAhead,lengthHistoricoList,emisora,trainSize,CList,fit_interceptList):
    total_modelos=len(nFeaturesList)*len(lengthHistoricoList)*len(CList)*len(fit_interceptList)
    scoreUsed=[]
    nFeaturesUsed=[]
    lengthHistoricoUsed=[]
    CUsed=[]
    fit_interceptUsed=[]
    count=0
    for a in nFeaturesList:
        for b in lengthHistoricoList:
            for c in CList:
                for d in fit_interceptList:
                        print("nFeatures es " + str(a) + ", lengthHistorico es " + str(b) + ", C es " + str(c) + ", fit_intercept es " + str(d))
                        try:
                            score=Score(nFeatures=a,nAhead=nAhead,
                                    lengthHistorico=b,emisora=emisora,trainSize=trainSize,C=c,fit_intercept=d)
                            scoreUsed.append(score)
                            print("el nFeatures usado es:")  
                            print(a)
                            nFeaturesUsed.append(a)
                            print("el lengthHistorico usado es:")
                            print(b)
                            lengthHistoricoUsed.append(b)
                            print("el C usado es:")
                            print(c)
                            CUsed.append(c)
                            print("el fit_intercept usado es:")
                            print(d)
                            fit_interceptUsed.append(d)
                        except ValueError:
                            pass
                        count=count+1
                        print("modelo "+ str(count) + " terminado de " +str(total_modelos) + " en total")
                    
    d={'score':scoreUsed,'nFeatures':nFeaturesUsed,'lengthHistorico':lengthHistoricoUsed,'C':CUsed,'fit_intercept':fit_interceptUsed}
    parametros=pd.DataFrame(d)
    parameters=parametros.sort_values(['score']).reset_index()
    return parameters

def fullTrain(fechaActual,nBack,nFeaturesList,nAhead,lengthHistoricoList,emisora,trainSize,CList,fit_interceptList):
    pathData="model/data/"+emisora+".csv"
    amov=pd.read_csv(pathData,header=6,sep=",")[::-1].reset_index(drop=True) 
    precios=amov['PRECIO']
    fechas=amov['Date']
    parameters=gridSearch(nFeaturesList=nFeaturesList,nAhead=nAhead,lengthHistoricoList=lengthHistoricoList,emisora=emisora,trainSize=trainSize,CList=CList,fit_interceptList=fit_interceptList)
    bestParameters=parameters.values[-1].tolist()
    print(bestParameters[1])
    nFeatures=bestParameters[2] #best nFeatures
    lengthHistorico=bestParameters[3] #best lengthHistorico
    C=bestParameters[4] #best C
    fit_intercept=bestParameters[5] #best fit_intercept
    features=buildFeatures(precios,fechas,nFeatures)
    label=buildLabel(precios,fechas,nAhead,nFeatures)
    labels=list(label.values())
    observations=list(features.values())[0:len(labels)]
    dates=list(label.keys())
    df=pd.concat([pd.DataFrame(observations),pd.DataFrame(labels),pd.DataFrame(dates)],axis=1)
    df.columns=["day"+str(i) for i in range(1,nFeatures+1)]+["target","fecha"]
    lr=LogisticRegression(C=C,fit_intercept=fit_intercept)
    lr.fit(df.iloc[0:df.shape[0]-nBack,0:nFeatures],df.iloc[0:df.shape[0]-nBack,nFeatures])
    fullData=buildFeatures(precios,fechas,nFeatures)
    prediccion=lr.predict(np.array(fullData[fechaActual]).reshape(1,-1))
    probabilidad=lr.predict_proba(np.array(fullData[fechaActual]).reshape(1,-1))
    return prediccion,probabilidad	

		#
	#
@app.route("/homeModeloApoyo")  
def homeModeloApoyo():
    return render_template('modeloApoyo.html')

@app.route("/modeloApoyo",methods=['POST','GET'])  
def modeloApoyo():
    emisora=request.form.get('emisora',type=str)	
    fechaActual=request.form.get('fechaActual',type=str)
    nAhead=request.form.get('nAhead',type=int)
    nBack=request.form.get('nBack',type=int)
    trainSize=request.form.get('trainSize',type=float)
    nFeaturesList=[7,9,11,13,15]
    lengthHistoricoList=[30,45,60,75,90,105,120,135,150]
    CList=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    fit_interceptList=[True,False]
    resultado=fullTrain(fechaActual=fechaActual,nBack=nBack,nFeaturesList=nFeaturesList,nAhead=nAhead,lengthHistoricoList=lengthHistoricoList,emisora=emisora,trainSize=trainSize,CList=CList,fit_interceptList=fit_interceptList)
    prediccion=resultado[0]
    probabilidad=resultado[1]
    probabilidad=probabilidad.tolist()	
    probabilidadBajada=probabilidad[0][0]
    probabilidadSubida=probabilidad[0][1]		
    return render_template("resultado.html",nAhead=nAhead,fechaActual=fechaActual,probabilidadBajada=probabilidadBajada,probabilidadSubida=probabilidadSubida)	
     

 
   
if __name__ == "__home__":
    #app.run(debug=True,port=5000)
	app.run(debug=True)
print('You can check the website now!')