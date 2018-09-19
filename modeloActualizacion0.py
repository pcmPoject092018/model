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
                rocValues.append((l[i+N-1]-l[i])/l[i])
        return rocValues
    
    def extractData(self):
        amov=pd.read_csv("C:/Users/USUARIO/Downloads/americamovil.csv",header=6,sep=";")
        amov['Date']=amov['Date'].astype(str)
        Date=[x.replace('/','-') for x in amov['Date']]
        Date=[datetime.datetime.strptime(x,'%d-%m-%Y').date() for x in Date]
        amov['Date']=Date
        amov=amov.sort_values('Date')
        amov['PX_LAST']=[float(x.replace(',','.')) for x in amov['PX_LAST']]
        TS=np.array(amov['PX_LAST'])
        tasa=self.ROC(TS.reshape(-1).tolist(),self._lengthTasa)
        return tasa
    
    def plotData(self):
        tasa=self.extractData()
        plt.figure(figsize=(18,9))
        plt.plot(range(len(tasa)),tasa)
        plt.show()
        
    def createBatches(self):
        tasa=self.extractData()
        TS=np.array(tasa)
        all_data_train=TS[(len(TS)%self._batch_size):]
        all_batches_train=all_data_train.reshape(-1,self._batch_size,1)
        print(len(all_batches_train))
        all_data_test=TS[((len(TS)%self._batch_size)+self._overlapSize):-self._overlapSize]
        all_batches_test=all_batches_test=all_data_test.reshape(-1,self._batch_size,1)
        print(len(all_batches_test))
        all_batches_train=all_batches_train[0:len(all_batches_test)]
        print(len(all_batches_train))
        return all_batches_train,all_batches_test

    def createTrainTestBatch(self):
        all_batches_train,all_batches_test=self.createBatches()
        X_test=all_batches_train[self._testBatchIndex].reshape(-1,self._batch_size,1)
        Y_test=all_batches_test[self._testBatchIndex].reshape(-1,self._batch_size,1)
        all_batches_train=all_batches_train[0:(self._testBatchIndex-1)]
        all_batches_test=all_batches_test[0:(self._testBatchIndex-1)]
        return all_batches_train,all_batches_test,X_test,Y_test

    def modelo(self):
        all_batches_train,all_batches_test,X_test,Y_test=self.createTrainTestBatch()
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
                        sess.run(training_op,feed_dict={X:all_batches_train,y:all_batches_test})
            if ep%100==0:
                mse=loss.eval(feed_dict={X:all_batches_train,y:all_batches_test})
                print(ep,"\tMSE:",mse)
            pred=X_test.reshape(-1,self._batch_size,1)        
            prediction=sess.run(outputs,feed_dict={X:pred})
        return prediction
    
    def plotPrediction(self):
        all_batches_train,all_batches_test,X_test,Y_test=self.createTrainTestBatch()
        X_test=X_test.reshape(-1).tolist()
        X_test=[i*100 for i in X_test]
        print("X_test is:")
        print(X_test)
        plt.plot(range(len(X_test)),X_test)
        plt.show()
        prediction=self.modelo()
        p=prediction.reshape(-1).tolist()
        p=[i*100 for i in p]
        print("prediction is:")
        print(p)
        r=Y_test.reshape(-1).tolist()
        r=[i*100 for i in r]
        print("real is:")
        print(r)
        plt.plot(range(len(p)),p,'r',label="prediction")
        plt.plot(range(len(p)),r,'b',label="real")
        plt.legend()
        plt.axvspan(0, 15, facecolor='0.5', alpha=0.5)
        plt.show()
        print(self.RSME(p,r))
        return p,r