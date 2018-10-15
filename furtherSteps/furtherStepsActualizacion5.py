#Step 1
current=0
fecha7DiasSiguientes=fecha7Dias[0]
print(fecha7DiasSiguientes)
#check data
m=TFModel(batch_size=14,lengthTasa=8,f_horizon=14,overlapSize=7,random_seed=activations[0],neurons=neurons,
          activation=activations[0],epochs=epochs[0],learning_rate=learning_rate[0],current=current)
r,s,t=m.createBatchesFecha()
print(t)

#middle step
horaInicio=datetime.datetime.now()
print(horaInicio)

p=gridSearch(activations,neurons,learning_rate,epochs,random_seed,current,fecha7DiasSiguientes)

p.to_csv("D/model/current6.csv",index=False)
print("p se escribio correctamente")
horaFinal=datetime.datetime.now()
print(horaFinal)
print(horaFinal-horaInicio)

p=pd.read_csv("D:/model/current.csv")
import ast
p['prediction']=[ast.literal_eval(i) for i in p['prediction']]

#Step 2
topN=3
bestPredictions=[np.array(p.loc[i,'prediction']) for i in range(topN)]
finalPrediction=np.mean(bestPredictions,axis=0)
print(finalPrediction)
m=TFModel(batch_size=14,lengthTasa=8,f_horizon=14,overlapSize=7,random_seed=activations[0],neurons=neurons[0],
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
    path='D:/model/predicciones/prediccionFinal.csv'
    df.to_csv(path,index=False)        
    return df
df=writeCSVFinalBatch()

def writeCSV(number):
    #finalPrediction
    #last_batch
    #precios_semana
    #finalDate
    df=pd.DataFrame({'fecha':finalDate,'prediccion':finalPrediction,'real':last_batch,'precios':precios_semana})
    path='D:/model/predicciones/prediccion'+str(number)+'.csv'       
    df.to_csv(path,index=False)        
    return df
df=writeCSV(1)