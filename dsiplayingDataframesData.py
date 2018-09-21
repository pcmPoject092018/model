import pandas as pd
import datetime
import numpy as np
df=pd.read_csv("D:/model/reciente.csv")
print(df)
print(df.dtypes)

def ROC(l,N):
    rocValues=[]
    for i in range(len(l)):
        if i+N-1 in range(len(l)):
            rocValues.append(100*(l[i+N-1]-l[i])/l[i])
    return rocValues
    
def ROCFecha(l,N):
    rocFechas=[]
    for i in range(len(l)):
        if i+N-1 in range(len(l)):
            rocFechas.append(l[i+N-1])
    return rocFechas
    
def ROCPrecios(l,N):
    rocPrecios=[]
    for i in range(len(l)):
        if i+N-1 in range(len(l)):
            rocPrecios.append(l[i+N-1])
    return rocPrecios        
    

df['Fecha']=df['Fecha'].astype(str)
Fecha=[x.replace('.','-') for x in df['Fecha']]
Fecha=[datetime.datetime.strptime(x,'%d-%m-%Y').date() for x in Fecha]
df['Fecha']=Fecha
df=df.sort_values('Fecha')

TS=np.array(df['Cierre'])
TSFecha=np.array(df['Fecha'])
tasa=ROC(TS.reshape(-1).tolist(),8)
fecha=ROCFecha(TSFecha.reshape(-1),8)
precios=ROCPrecios(TS.reshape(-1),8)
print(fecha)
print(tasa)
print(precios)

fecha_str=[i.strftime("%d-%m-%Y") for i in fecha]

source=pd.DataFrame({'fecha':fecha_str,'tasa':tasa,'precios':precios})
print(source)

dataframe1=source.iloc[18:25,]
dataframe2=source.iloc[23:30,]
dataframe3=source.iloc[28:35,]
dataframe4=source.iloc[33:40,]
dataframe5=source.iloc[38:45,]
dataframe6=source.iloc[43:50,]

dataframe1previous=source.iloc[11:18,]
dataframe2previous=source.iloc[16:23,]
dataframe3previous=source.iloc[21:28,]
dataframe4previous=source.iloc[26:33,]
dataframe5previous=source.iloc[31:38,]
dataframe6previous=source.iloc[36:43,]

dataframeprevious=source.iloc[41:48,]


dataframe1.to_csv("D:/model/dataframe1.csv",index=False)
dataframe2.to_csv("D:/model/dataframe2.csv",index=False)
dataframe3.to_csv("D:/model/dataframe3.csv",index=False)
dataframe4.to_csv("D:/model/dataframe4.csv",index=False)
dataframe5.to_csv("D:/model/dataframe5.csv",index=False)
dataframe6.to_csv("D:/model/dataframe6.csv",index=False)

dataframe1previous.to_csv("D:/model/dataframe1previous.csv",index=False)
dataframe2previous.to_csv("D:/model/dataframe2previous.csv",index=False)
dataframe3previous.to_csv("D:/model/dataframe3previous.csv",index=False)
dataframe4previous.to_csv("D:/model/dataframe4previous.csv",index=False)
dataframe5previous.to_csv("D:/model/dataframe5previous.csv",index=False)
dataframe6previous.to_csv("D:/model/dataframe6previous.csv",index=False)

dataframeprevious.to_csv("D:/model/dataframeprevious.csv",index=False)

