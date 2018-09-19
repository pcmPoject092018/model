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
    
    def __init__(self,batch_size,lengthTasa,f_horizon,overlapSize,random_seed,neurons,activation,epochs,learning_rate,current):
        #
        self._current=current
        #
        self._batch_size=batch_size
        self._lengthTasa=lengthTasa
        self._f_horizon=f_horizon
        self._overlapSize=overlapSize
        self._random_seed=random_seed
        self._neurons=neurons
        self._activation=activation
        self._learning_rate=learning_rate
        self._epochs=epochs
        self._tasa, self._fecha, self._precios = self.extractData()
        self._all_batches_train, self._all_batches_test, self._last_batch = self.createBatches()
        self._all_batches_train_fecha, self._all_batches_test_fecha, self._last_batch_fecha = self.createBatchesFecha()
        self._all_batches_train_precios, self._all_batches_test_precios, self._last_batch_precios = self.createBatchesPrecios()
            
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
        pathData='C:/Users/USUARIO/Documents/stocksModel/data/americamovil.csv'
        amov=pd.read_csv(pathData,header=0,sep=",")
        amov['Fecha']=amov['Fecha'].astype(str)
        Fecha=[x.replace('.','-') for x in amov['Fecha']]
        Fecha=[datetime.datetime.strptime(x,'%d-%m-%Y').date() for x in Fecha]
        amov['Fecha']=Fecha
        amov=amov.sort_values('Fecha')
        if self._current==0:
            amov=amov
        else:
            amov=amov.iloc[0:self._current,]
        TS=np.array(amov['Cierre'])
        TSFecha=np.array(amov['Fecha'])
        tasa=self.ROC(TS.reshape(-1).tolist(),self._lengthTasa)
        fecha=self.ROCFecha(TSFecha.reshape(-1),self._lengthTasa)
        precios=self.ROCPrecios(TS.reshape(-1),self._lengthTasa)
        return tasa, fecha, precios
    
    def originalData(self):
        pathData='C:/Users/USUARIO/Documents/stocksModel/data/americamovil.csv'
        amov=pd.read_csv(pathData,header=0,sep=",")
        amov['Fecha']=amov['Fecha'].astype(str)
        Fecha=[x.replace('.','-') for x in amov['Fecha']]
        Fecha=[datetime.datetime.strptime(x,'%d-%m-%Y').date() for x in Fecha]
        amov['Fecha']=Fecha
        amov=amov.sort_values('Fecha')
        if self._current==0:
            amov=amov
        else:
            amov=amov.iloc[0:self._current,]
        return amov
    
    #def plotData(self):
    #    tasa=self._tasa[0:self._batch_size]
    #    fecha=self._fecha[0:self._batch_size]
    #    plt.figure(figsize=(18,9))
    #    plt.plot(fecha,tasa)
    #    plt.xticks(fecha, rotation='vertical')
    #    plt.show()
    
    def plotLastBatch(self):
        tasa=self._last_batch.reshape(-1).tolist()
        fecha=self._last_batch_fecha.reshape(-1).tolist()
        plt.figure(figsize=(18,9))
        plt.plot(fecha,tasa)
        plt.xticks(fecha, rotation='vertical')
        plt.show()
    
    def createBatches(self):
        TS=np.array(self._tasa)
        all_data_train=TS[(len(TS)%self._batch_size):]
        all_batches_train=all_data_train.reshape(-1,self._batch_size,1)
        all_data_test=TS[((len(TS)%self._batch_size)+self._overlapSize):-self._overlapSize]
        all_batches_test=all_data_test.reshape(-1,self._batch_size,1)
        last_batch=all_batches_train[-1]
        all_batches_train=all_batches_train[0:len(all_batches_test)] #length of training batches should be equal to length of testing batches
        return all_batches_train,all_batches_test,last_batch
    
    def createBatchesFecha(self):
        TSFecha=np.array(self._fecha)
        all_data_train_fecha=TSFecha[(len(TSFecha)%self._batch_size):]
        all_batches_train_fecha=all_data_train_fecha.reshape(-1,self._batch_size,1)
        all_data_test_fecha=TSFecha[((len(TSFecha)%self._batch_size)+self._overlapSize):-self._overlapSize]
        all_batches_test_fecha=all_data_test_fecha.reshape(-1,self._batch_size,1)
        last_batch_fecha=all_batches_train_fecha[-1]
        all_batches_train_fecha=all_batches_train_fecha[0:len(all_batches_test_fecha)] #length of training batches should be equal to length of testing batches
        return all_batches_train_fecha,all_batches_test_fecha,last_batch_fecha
    
    def createBatchesPrecios(self):
        TSPrecios=np.array(self._precios)
        all_data_train_precios=TSPrecios[(len(TSPrecios)%self._batch_size):]
        all_batches_train_precios=all_data_train_precios.reshape(-1,self._batch_size,1)
        all_data_test_precios=TSPrecios[((len(TSPrecios)%self._batch_size)+self._overlapSize):-self._overlapSize]
        all_batches_test_precios=all_data_test_precios.reshape(-1,self._batch_size,1)
        last_batch_precios=all_batches_train_precios[-1]
        all_batches_train_precios=all_batches_train_precios[0:len(all_batches_test_precios)] #length of training batches should be equal to length of testing batches
        return all_batches_train_precios,all_batches_test_precios,last_batch_precios

    def modelo(self):
        tf.reset_default_graph()
        tf.set_random_seed(self._random_seed)
        inputs=1
        output=1
        X=tf.placeholder(tf.float32,[None,self._batch_size,inputs])
        y=tf.placeholder(tf.float32,[None,self._batch_size,output])
        #basic_cell=tf.contrib.rnn.BasicRNNCell(num_units=self._hidden,activation=self._activation)
        cells=[tf.contrib.rnn.BasicRNNCell(num_units=self._neurons[i],activation=tf.nn.elu) for i in range(len(self._neurons))]
        multi_cells=tf.contrib.rnn.MultiRNNCell(cells)
        #rnn_output,states=tf.nn.dynamic_rnn(basic_cell,X,dtype=tf.float32)
        rnn_output,states=tf.nn.dynamic_rnn(multi_cells,X,dtype=tf.float32)
        stacked_rnn_output=tf.reshape(rnn_output,[-1,self._batch_size,self._neurons[-1]])
        stacked_outputs=tf.layers.dense(stacked_rnn_output,output)
        outputs=tf.reshape(stacked_outputs,[-1,self._batch_size,output])
        loss=tf.reduce_mean(tf.square(outputs-y))
        optimizer=tf.train.AdamOptimizer(learning_rate=self._learning_rate)
        training_op=optimizer.minimize(loss)
        init=tf.global_variables_initializer()
        with tf.Session() as sess:
            init.run()
            for ep in range(self._epochs):
                        sess.run(training_op,feed_dict={X:self._all_batches_train,y:self._all_batches_test})
            if ep%100==0:
                mse=loss.eval(feed_dict={X:self._all_batches_train,y:self._all_batches_test})
                print(ep,"\tMSE:",mse)
            lastBatchPrediction=sess.run(outputs,feed_dict={X:self._last_batch.reshape(-1,self._batch_size,1)})
        return lastBatchPrediction
        
    def plotPrediction(self,fecha7DiasSiguientes):
        #prediction
        lastBatchPrediction=self.modelo()
        lastBatchPrediction=lastBatchPrediction.reshape(-1).tolist()
        #fecha
        last_batch_fecha=self._last_batch_fecha.reshape(-1).tolist()
        last_batch_fecha=[i.strftime("%d-%m-%Y") for i in last_batch_fecha]
        #fecha7DiasSiguientes=[datetime.datetime.strptime(i,'%d-%m-%Y').date() for i in fecha7DiasSiguientes]
        #fecha7DiasSiguientes=[i.strftime('%d-%m-%Y') for i in fecha7DiasSiguientes]
        lastBatchFecha=last_batch_fecha[7:]+fecha7DiasSiguientes[7:]
        print("lastBatchFecha is:")
        print(lastBatchFecha)
        print(len(lastBatchFecha))
        #real
        lastBatchReal=self._last_batch.reshape(-1).tolist()
        lastBatchReal=lastBatchReal[7:]
        print("second half of lastBatch is:")
        print(lastBatchReal)
        firstHalfPredictionLastBatchPrediction=lastBatchPrediction[0:7]
        #error
        e=self.RSME(lastBatchReal,firstHalfPredictionLastBatchPrediction)
        lastBatchReal=lastBatchReal+[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
        print("error is:")
        print(e)
        print("prediction obtained by fitting last_batch is:")
        print(lastBatchPrediction)
        print("plot of last batch prediction is:")
        plt.xticks(range(len(lastBatchPrediction)),lastBatchFecha,rotation='vertical')
        plt.axvspan(0, self._overlapSize-1, facecolor='0.5', alpha=0.5)
        plt.plot(lastBatchPrediction)
        plt.plot(lastBatchReal)
        plt.show()
        return lastBatchPrediction,e
    