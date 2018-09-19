import tensorflow as tf
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import tensorflow.contrib.rnn as rnn
import tensorflow.contrib.layers as tflayers

from sklearn.preprocessing import MinMaxScaler

import math
import datetime


class TFModel(object):
    
    def __init__(self,batch_size,lengthTasa,f_horizon,overlapSize,testBatchIndex,random_seed,hidden,activation,epochs,learning_rate):
        self._batch_size=batch_size
        self._lengthTasa=lengthTasa
        self._f_horizon=f_horizon
        self._overlapSize=overlapSize
        self._testBatchIndex=testBatchIndex
        self._random_seed=random_seed
        self._hidden=hidden
        self._activation=activation
        self._learning_rate=learning_rate
        self._epochs=epochs
        self._tasa, self._fecha, self._precios = self.extractData()
        self._all_batches_train, self._all_batches_test, self._last_batch = self.createBatches()
        self._all_batches_train_fecha, self._all_batches_test_fecha, self._last_batch_fecha = self.createBatchesFecha()
        self._all_batches_train_precios, self._all_batches_test_precios, self._last_batch_precios = self.createBatchesPrecios()
        self._all_batches_train_previousIndex, self._all_batches_test_previousIndex, self._X_test_currentIndex, self._Y_test_currentIndex = self.createTrainTestBatch()
        self._all_batches_train_fecha_previousIndex, self._all_batches_test_fecha_previousIndex, self._X_test_fecha_currentIndex, self._Y_test_fecha_currentIndex = self.createTrainTestBatchFecha()
        self._all_batches_train_precios_previousIndex, self._all_batches_test_precios_previousIndex, self._X_test_precios_currentIndex, self._Y_test_precios_currentIndex = self.createTrainTestBatchPrecios()
     
            
    def RSME(self,lista1,lista2):
        lista=[]
        for i in range(len(lista1)):
            square=(lista1[i]-lista2[i])*(lista1[i]-lista2[i])
            lista.append(square)
        rsme=sum(lista)/len(lista)
        return math.sqrt(rsme)   
    
    def ROC(self,l,N):
        rocValues=[]
        for i in range(len(l)):
            if i+N-1 in range(len(l)):
                rocValues.append(100*(l[i+N-1]-l[i])/l[i])
        return rocValues
    
    def ROCFecha(self,l,N):
        rocFechas=[]
        for i in range(len(l)):
            if i+N-1 in range(len(l)):
                rocFechas.append(l[i+N-1])
        return rocFechas
    
    def ROCPrecios(self,l,N):
        rocPrecios=[]
        for i in range(len(l)):
            if i+N-1 in range(len(l)):
                rocPrecios.append(l[i+N-1])
        return rocPrecios        
    
    def extractData(self):
        amov=pd.read_csv("C:/Users/USUARIO/Downloads/americamovil.csv",header=6,sep=";")
        amov['Date']=amov['Date'].astype(str)
        Date=[x.replace('/','-') for x in amov['Date']]
        Date=[datetime.datetime.strptime(x,'%d-%m-%Y').date() for x in Date]
        amov['Date']=Date
        amov=amov.sort_values('Date')
        amov['Date']=[str(i) for i in amov['Date']]
        amov['PX_LAST']=[float(x.replace(',','.')) for x in amov['PX_LAST']]
        #amov=amov.iloc[:-35,]
        TS=np.array(amov['PX_LAST'])
        TSFecha=np.array(amov['Date'])
        tasa=self.ROC(TS.reshape(-1).tolist(),self._lengthTasa)
        fecha=self.ROCFecha(TSFecha.reshape(-1),self._lengthTasa)
        precios=self.ROCPrecios(TS.reshape(-1),self._lengthTasa)
        return tasa,fecha,precios
    
    def originalData(self):
        amov=pd.read_csv("C:/Users/USUARIO/Downloads/americamovil.csv",header=6,sep=";")
        amov['Date']=amov['Date'].astype(str)
        Date=[x.replace('/','-') for x in amov['Date']]
        Date=[datetime.datetime.strptime(x,'%d-%m-%Y').date() for x in Date]
        amov['Date']=Date
        amov['PX_LAST']=[float(x.replace(',','.')) for x in amov['PX_LAST']]
        amov=amov.sort_values('Date')
        #amov=amov.iloc[:-35,]
        return amov
    
    def plotData(self):
        #tasa,fecha,precios=self.extractData()
        #tasa=tasa[0:self._batch_size]
        tasa=self._tasa[0:self._batch_size]
        #fecha=fecha[0:self._batch_size]
        fecha=self._fecha[0:self._batch_size]
        plt.figure(figsize=(18,9))
        plt.plot(fecha,tasa)
        plt.xticks(fecha, rotation='vertical')
        plt.show()
        
    def createBatches(self):
        #tasa,fecha,precios=self.extractData()
        #TS=np.array(tasa)
        TS=np.array(self._tasa)
        all_data_train=TS[(len(TS)%self._batch_size):]
        all_batches_train=all_data_train.reshape(-1,self._batch_size,1)
        all_data_test=TS[((len(TS)%self._batch_size)+self._overlapSize):-self._overlapSize]
        all_batches_test=all_data_test.reshape(-1,self._batch_size,1)
        last_batch=all_batches_train[-1]
        all_batches_train=all_batches_train[0:len(all_batches_test)] #length of training batches should be equal to length of testing batches
        return all_batches_train,all_batches_test,last_batch
    
    def createBatchesFecha(self):
        #tasa,fecha,precios=self.extractData()
        #TSFecha=np.array(fecha)
        TSFecha=np.array(self._fecha)
        all_data_train_fecha=TSFecha[(len(TSFecha)%self._batch_size):]
        all_batches_train_fecha=all_data_train_fecha.reshape(-1,self._batch_size,1)
        all_data_test_fecha=TSFecha[((len(TSFecha)%self._batch_size)+self._overlapSize):-self._overlapSize]
        all_batches_test_fecha=all_data_test_fecha.reshape(-1,self._batch_size,1)
        last_batch_fecha=all_batches_train_fecha[-1]
        all_batches_train_fecha=all_batches_train_fecha[0:len(all_batches_test_fecha)] #length of training batches should be equal to length of testing batches
        return all_batches_train_fecha,all_batches_test_fecha,last_batch_fecha
    
    def createBatchesPrecios(self):
        #tasa,fecha,precios=self.extractData()
        #TSPrecios=np.array(precios)
        TSPrecios=np.array(self._precios)
        all_data_train_precios=TSPrecios[(len(TSPrecios)%self._batch_size):]
        all_batches_train_precios=all_data_train_precios.reshape(-1,self._batch_size,1)
        all_data_test_precios=TSPrecios[((len(TSPrecios)%self._batch_size)+self._overlapSize):-self._overlapSize]
        all_batches_test_precios=all_data_test_precios.reshape(-1,self._batch_size,1)
        last_batch_precios=all_batches_train_precios[-1]
        all_batches_train_precios=all_batches_train_precios[0:len(all_batches_test_precios)] #length of training batches should be equal to length of testing batches
        return all_batches_train_precios,all_batches_test_precios,last_batch_precios
    
    def createTrainTestBatch(self):
        #all_batches_train,all_batches_test,last_batch=self.createBatches()
        #X_test=all_batches_train[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #Y_test=all_batches_test[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #all_batches_train=all_batches_train[0:(self._testBatchIndex-1)]
        #all_batches_test=all_batches_test[0:(self._testBatchIndex-1)]
        #return all_batches_train,all_batches_test,X_test,Y_test
        #
        #X_test_currentIndex=all_batches_train[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #Y_test_currentIndex=all_batches_test[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #all_batches_train_previousIndex=all_batches_train[0:(self._testBatchIndex-1)]
        #all_batches_test_previousIndex=all_batches_test[0:(self._testBatchIndex-1)]
        X_test_currentIndex=self._all_batches_train[self._testBatchIndex].reshape(-1,self._batch_size,1)
        Y_test_currentIndex=self._all_batches_test[self._testBatchIndex].reshape(-1,self._batch_size,1)
        all_batches_train_previousIndex=self._all_batches_train[0:(self._testBatchIndex-1)]
        all_batches_test_previousIndex=self._all_batches_test[0:(self._testBatchIndex-1)]
        return all_batches_train_previousIndex,all_batches_test_previousIndex,X_test_currentIndex,Y_test_currentIndex

    def createTrainTestBatchFecha(self):
        #all_batches_train_fecha,all_batches_test_fecha,last_batch_fecha=self.createBatchesFecha()
        #X_test_fecha=all_batches_train_fecha[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #Y_test_fecha=all_batches_test_fecha[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #all_batches_train_fecha=all_batches_train_fecha[0:(self._testBatchIndex-1)]
        #all_batches_test_fecha=all_batches_test_fecha[0:(self._testBatchIndex-1)]
        #return all_batches_train_fecha,all_batches_test_fecha,X_test_fecha,Y_test_fecha
        #
        #X_test_fecha_currentIndex=all_batches_train_fecha[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #Y_test_fecha_currentIndex=all_batches_test_fecha[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #all_batches_train_fecha_previousIndex=all_batches_train_fecha[0:(self._testBatchIndex-1)]
        #all_batches_test_fecha_previousIndex=all_batches_test_fecha[0:(self._testBatchIndex-1)]
        X_test_fecha_currentIndex=self._all_batches_train_fecha[self._testBatchIndex].reshape(-1,self._batch_size,1)
        Y_test_fecha_currentIndex=self._all_batches_test_fecha[self._testBatchIndex].reshape(-1,self._batch_size,1)
        all_batches_train_fecha_previousIndex=self._all_batches_train_fecha[0:(self._testBatchIndex-1)]
        all_batches_test_fecha_previousIndex=self._all_batches_test_fecha[0:(self._testBatchIndex-1)]
        return all_batches_train_fecha_previousIndex,all_batches_test_fecha_previousIndex,X_test_fecha_currentIndex,Y_test_fecha_currentIndex
    
    def createTrainTestBatchPrecios(self):
        #all_batches_train_precios,all_batches_test_precios,last_batch_precios=self.createBatchesPrecios()
        #X_test_precios=all_batches_train_precios[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #Y_test_precios=all_batches_test_precios[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #all_batches_train_precios=all_batches_train_precios[0:(self._testBatchIndex-1)]
        #all_batches_test_precios=all_batches_test_precios[0:(self._testBatchIndex-1)]
        #return all_batches_train_precios,all_batches_test_precios,X_test_precios,Y_test_precios
        #
        #X_test_precios_currentIndex=all_batches_train_precios[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #Y_test_precios_currentIndex=all_batches_test_precios[self._testBatchIndex].reshape(-1,self._batch_size,1)
        #all_batches_train_precios_previousIndex=all_batches_train_precios[0:(self._testBatchIndex-1)]
        #all_batches_test_precios_previousIndex=all_batches_test_precios[0:(self._testBatchIndex-1)]
        X_test_precios_currentIndex=self._all_batches_train_precios[self._testBatchIndex].reshape(-1,self._batch_size,1)
        Y_test_precios_currentIndex=self._all_batches_test_precios[self._testBatchIndex].reshape(-1,self._batch_size,1)
        all_batches_train_precios_previousIndex=self._all_batches_train_precios[0:(self._testBatchIndex-1)]
        all_batches_test_precios_previousIndex=self._all_batches_test_precios[0:(self._testBatchIndex-1)]
        return all_batches_train_precios_previousIndex,all_batches_test_precios_previousIndex,X_test_precios_currentIndex,Y_test_precios_currentIndex  
    
    def modelo(self):
        #all_batches_train,all_batches_test,X_test,Y_test=self.createTrainTestBatch()
        #all_batches_train,all_batches_test,last_batch=self.createBatches() # for last batch prediction without testing data
        tf.reset_default_graph()
        tf.set_random_seed(self._random_seed)
        inputs=1
        output=1
        X=tf.placeholder(tf.float32,[None,self._batch_size,inputs])
        y=tf.placeholder(tf.float32,[None,self._batch_size,output])
        basic_cell=tf.contrib.rnn.BasicRNNCell(num_units=self._hidden,activation=self._activation)
        rnn_output,states=tf.nn.dynamic_rnn(basic_cell,X,dtype=tf.float32)
        stacked_rnn_output=tf.reshape(rnn_output,[-1,self._hidden])
        stacked_outputs=tf.layers.dense(stacked_rnn_output,output)
        outputs=tf.reshape(stacked_outputs,[-1,self._batch_size,output])
        loss=tf.reduce_mean(tf.square(outputs-y))
        optimizer=tf.train.AdamOptimizer(learning_rate=self._learning_rate)
        training_op=optimizer.minimize(loss)
        init=tf.global_variables_initializer()
        with tf.Session() as sess:
            init.run()
            for ep in range(self._epochs):
                        #sess.run(training_op,feed_dict={X:all_batches_train,y:all_batches_test})
                        #
                        #sess.run(training_op,feed_dict={X:all_batches_train_previousIndex,y:all_batches_test_previousIndex})
                        sess.run(training_op,feed_dict={X:self._all_batches_train_previousIndex,y:self._all_batches_test_previousIndex})
            if ep%100==0:
                #mse=loss.eval(feed_dict={X:all_batches_train,y:all_batches_test})
                #
                #mse=loss.eval(feed_dict={X:all_batches_train_previousIndex,y:all_batches_test_previousIndex})
                mse=loss.eval(feed_dict={X:self._all_batches_train_previousIndex,y:self._all_batches_test_previousIndex})
                print(ep,"\tMSE:",mse)
            #pred=X_test.reshape(-1,self._batch_size,1) 
            #
            #pred=X_test_currentIndex.reshape(-1,self._batch_size,1)
            pred=self._X_test_currentIndex.reshape(-1,self._batch_size,1)
            prediction=sess.run(outputs,feed_dict={X:pred})
            #lastBatchPrediction=sess.run(outputs,feed_dict={X:last_batch.reshape(-1,self._batch_size,1)})
            lastBatchPrediction=sess.run(outputs,feed_dict={X:self._last_batch.reshape(-1,self._batch_size,1)})
        return prediction,lastBatchPrediction
        
    def plotPrediction(self):
        #all_batches_train,all_batches_test,X_test,Y_test=self.createTrainTestBatch()
        #all_batches_train_fecha,all_batches_test_fecha,X_test_fecha,Y_test_fecha=self.createTrainTestBatchFecha()
        #X_test=X_test.reshape(-1).tolist()
        #
        #X_test_currentIndex=X_test_currentIndex.reshape(-1).tolist()
        X_test_currentIndex=self._X_test_currentIndex.reshape(-1).tolist()
        #X_test_fecha=X_test_fecha.reshape(-1).tolist()
        #
        #X_test_fecha_currentIndex=X_test_fecha_currentIndex.reshape(-1).tolist()
        X_test_fecha_currentIndex=self._X_test_fecha_currentIndex.reshape(-1).tolist()
        print("X_test_currentIndex is:")
        print(X_test_currentIndex)
        #plt.plot(X_test_fecha,X_test)
        plt.plot(X_test_fecha_currentIndex,X_test_currentIndex)
        #plt.xticks(X_test_fecha, rotation='vertical')
        plt.xticks(X_test_fecha_currentIndex,rotation='vertical')
        plt.show()
        prediction,lastBatchPrediction=self.modelo()
        p=prediction.reshape(-1).tolist()
        lastBatchPrediction=lastBatchPrediction.reshape(-1).tolist()
        print("prediction obtained by fitting X_test_currentIndex is:")
        print(p)
        #r=Y_test.reshape(-1).tolist()
        #
        #r=Y_test_currentIndex.reshape(-1).tolist()
        r=self._Y_test_currentIndex.reshape(-1).tolist()
        #Y_test_fecha=Y_test_fecha.reshape(-1).tolist()
        #
        #Y_test_fecha_currentIndex=Y_test_fecha_currentIndex.reshape(-1).tolist()
        Y_test_fecha_currentIndex=self._Y_test_fecha_currentIndex.reshape(-1).tolist()
        print("real Y_test_currentIndex is:")
        print(r)
        #plt.plot(Y_test_fecha,p,'r',label="prediction")
        plt.plot(Y_test_fecha_currentIndex,p,'r',label="prediction")
        #plt.plot(Y_test_fecha,r,'b',label="real")
        plt.plot(Y_test_fecha_currentIndex,r,'b',label="real")
        #plt.xticks(Y_test_fecha, rotation='vertical')
        plt.xticks(Y_test_fecha_currentIndex,rotation='vertical')
        plt.legend()
        plt.axvspan(0, self._overlapSize-1, facecolor='0.5', alpha=0.5)
        plt.show()
        e=self.RSME(p,r)
        print("error is:")
        print(e)
        print("prediction obtained by fitting last_batch is:")
        print(lastBatchPrediction)
        print("plot of last batch prediction is:")
        plt.plot(range(len(lastBatchPrediction)),lastBatchPrediction)
        plt.axvspan(0, self._overlapSize-1, facecolor='0.5', alpha=0.5)
        plt.show()
        return p,r,e
    
    #def writeCSV(self,numero):
    def writeCSV(self):
        #all_batches_train_fecha,all_batches_test_fecha,X_test_fecha,Y_test_fecha=self.createTrainTestBatchFecha()
        #all_batches_train_precios,all_batches_test_precios,X_test_precios,Y_test_precios=self.createTrainTestBatchPrecios()
        #
        #Y_test_fecha=Y_test_fecha.reshape(-1).tolist()
        Y_test_fecha_currentIndex=self._Y_test_fecha_currentIndex.reshape(-1).tolist()
        #Y_test_precios=Y_test_precios.reshape(-1).tolist()
        Y_test_precios_currentIndex=self._Y_test_precios_currentIndex.reshape(-1).tolist()
        p,r,e=self.plotPrediction()
        #df=pd.DataFrame({'fecha':Y_test_fecha,'prediccion':p,'real':r,'precios':Y_test_precios})
        df=pd.DataFrame({'fecha':Y_test_fecha_currentIndex,'prediccion':p,'real':r,'precios':Y_test_precios_currentIndex})
        #path='C:/Users/USUARIO/Documents/stocksModel/predicciones/prediccion'+str(numero)+'.csv'
        path='C:/Users/USUARIO/Documents/stocksModel/predicciones/prediccion'+str((-1)*self._testBatchIndex)+'.csv'       
        df.to_csv(path,index=False)        
        return "terminado" 
    
    def writeCSVFinalBatch(self):
        #all_batches_train,all_batches_test,last_batch=self.createBatches()#for last  batch prediction without testing
        #all_batches_train_fecha,all_batches_test_fecha,last_batch_fecha=self.createBatchesFecha() # for last batch prediction without testing data
        #all_batches_train_precios,all_batches_test_precios,last_batch_precios=self.createBatchesPrecios() # for last batch prediction without testing data
        prediction,lastBatchPrediction=self.modelo()
        #last_batch=last_batch.reshape(-1).tolist()
        last_batch=self._last_batch.reshape(-1).tolist()
        #last_batch_fecha=last_batch_fecha.reshape(-1).tolist()
        last_batch_fecha=self._last_batch_fecha.reshape(-1).tolist()
        #last_batch_precios=last_batch_precios.reshape(-1).tolist()
        last_batch_precios=self._last_batch_precios.reshape(-1).tolist()
        lastBatchPrediction=lastBatchPrediction.reshape(-1).tolist()
        df=pd.DataFrame({'fecha':last_batch_fecha,'prediccion':lastBatchPrediction,'real':last_batch,'precios':last_batch_precios})
        path='C:/Users/USUARIO/Documents/stocksModel/predicciones/prediccionFinal.csv'
        df.to_csv(path,index=False)        
        return "terminado last batch"