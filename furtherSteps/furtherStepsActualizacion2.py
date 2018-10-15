#Step 1
activations=[tf.nn.elu,tf.nn.relu]
hidden=[100,500,1000]
learning_rate=[0.0001,0.001,0.005,0.0005]
epochs=[500,1000]
random_seed=[100,500,250]
current=-25
fecha7DiasSiguientes=["02-08-2018","03-08-2018","06-08-2018","07-08-2018","08-08-2018","09-08-2018","10-08-2018",
                     "13-08-2018","14-08-2018","15-08-2018","16-08-2018","17-08-2018","20-08-2018","21-08-2018"]
#check data
m=TFModel(batch_size=14,lengthTasa=8,f_horizon=14,overlapSize=7,random_seed=activations[0],hidden=hidden[0],
          activation=activations[0],epochs=epochs[0],learning_rate=learning_rate[0],current=current)
r,s,t=m.createBatchesFecha()
t

#middle step

import datetime
print(datetime.datetime.now())
p=gridSearch(activations,hidden,learning_rate,epochs,random_seed,current,fecha7DiasSiguientes)

p.to_csv("C:/Users/USUARIO/Documents/stocksModel/current2.csv",index=False)
print("p se escribio correctamente")

print(datetime.datetime.now())

p=pd.read_csv("C:/Users/USUARIO/Documents/stocksModel/current2.csv")
import ast
p['prediction']=[ast.literal_eval(i) for i in p['prediction']]

#Step 2
topN=2
bestPredictions=[np.array(p.loc[i,'prediction']) for i in range(topN)]
finalPrediction=np.mean(bestPredictions,axis=0)
print(finalPrediction)
m=TFModel(batch_size=14,lengthTasa=8,f_horizon=14,overlapSize=7,random_seed=activations[0],hidden=hidden[0],
          activation=activations[0],epochs=epochs[0],learning_rate=learning_rate[0],current=current)
all_train_batches,all_test_batches,last_batch=m.createBatches()
last_batch=last_batch.reshape(-1).tolist()
last_batch=last_batch[7:]+[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
finalDate=fecha7DiasSiguientes
plt.xticks(range(len(finalPrediction)),finalDate,rotation='vertical')
plt.plot(finalPrediction)
plt.plot(last_batch)
plt.show()

#step 3
all_train_batches_precios, all_test_batches_precios,last_batch_precios=m.createBatchesPrecios()
precios_semana=last_batch_precios[7:]
precios_semana=precios_semana.reshape(-1).tolist()+[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]

#step 4
def writeCSVFinalBatch():
    #last_batch
    #finalDate
    #last_batch_precios
    #finalPrediction
    df=pd.DataFrame({'fecha':finalDate,'prediccion':finalPrediction,'real':last_batch,'precios':precios_semana})
    path='C:/Users/USUARIO/Documents/stocksModel/predicciones/prediccionFinal.csv'
    df.to_csv(path,index=False)        
    return df
df=writeCSVFinalBatch()

def writeCSV(number):
    #finalPrediction
    #last_batch
    #precios_semana
    #finalDate
    df=pd.DataFrame({'fecha':finalDate,'prediccion':finalPrediction,'real':last_batch,'precios':precios_semana})
    path='C:/Users/USUARIO/Documents/stocksModel/predicciones/prediccion'+str(number)+'.csv'       
    df.to_csv(path,index=False)        
    return df
df=writeCSV(2)
