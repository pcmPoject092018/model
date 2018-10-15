activations=[tf.nn.elu,tf.nn.relu]
num_activations=len(activations)
neurons=[[100],[500],[1000],[100,50],[500,100],[100,100,50],[500,100,100],[100,100,100,50],[100,100,50,50]]
num_neurons=len(neurons)
learning_rate=[0.0001,0.001,0.005,0.0005]
num_learning_rate=len(learning_rate)
epochs=[300,500,1000]
num_epochs=len(epochs)
random_seed=[100,500,250]
num_random_seed=len(random_seed)
total_modelos=num_activations*num_neurons*num_learning_rate*num_epochs*num_random_seed
def gridSearch(activations,neurons,learning_rate,epochs,random_seed,current,fecha7DiasSiguientes):
    activationUsed=[]
    neuronsUsed=[]
    learning_rateUsed=[]
    epochsUsed=[]
    random_seedUsed=[]
    errorUsed=[]
    predictionObtained=[]
    count=0
    for a in activations:
        for b in neurons:
            for c in learning_rate:
                for d in epochs:
                    for e in random_seed:
                        m=TFModel(batch_size=14,lengthTasa=8,f_horizon=14,overlapSize=7,random_seed=e,neurons=b,activation=a,learning_rate=c,epochs=d,current=current)
                        p,error=m.plotPrediction(fecha7DiasSiguientes)
                        print("el error es:")
                        print(error)
                        errorUsed.append(error)
                        print("la prediccion obtenida es:")
                        print(p)
                        predictionObtained.append(p)
                        print("la activacion usada es:")
                        print(a)
                        activationUsed.append(a)
                        print("el neuron usado es:")
                        print(b)
                        neuronsUsed.append(b)
                        print("el learning rate usado es:")
                        print(c)
                        learning_rateUsed.append(c)
                        print("los epochs usados son:")
                        print(d)
                        epochsUsed.append(d)
                        print("el random seed usado es:")
                        print(e)
                        random_seedUsed.append(e)
                        count=count+1
                        print("modelo "+ str(count) + " terminado de " +str(total_modelos) + " en total")
                    
    d={'prediction':predictionObtained,'neurons':neuronsUsed,'activation':activationUsed,'epochs':epochsUsed,'random_seed':random_seedUsed,'error':errorUsed,'learning_rate':learning_rateUsed}
    parametros=pd.DataFrame(d)
    parameters=parametros.sort_values(['error']).reset_index()
    return parameters
fecha7Dias=[["06-09-2018","07-09-2018","10-09-2018","11-09-2018","12-09-2018","13-09-2018","14-09-2018","17-09-2018","18-09-2018","19-09-2018","20-09-2018","21-09-2018","24-09-2018","25-09-2018"],
            ["26-07-2018","27-07-2018","30-07-2018","31-07-2018","01-08-2018","02-08-2018","03-08-2018","06-08-2018","07-08-2018","08-08-2018","09-08-2018","10-08-2018","13-08-2018","14-08-2018"],
            ["02-08-2018","03-08-2018","06-08-2018","07-08-2018","08-08-2018","09-08-2018","10-08-2018","13-08-2018","14-08-2018","15-08-2018","16-08-2018","17-08-2018","20-08-2018","21-08-2018"],
            ["09-08-2018","10-08-2018","13-08-2018","14-08-2018","15-08-2018","16-08-2018","17-08-2018","20-08-2018","21-08-2018","22-08-2018","23-08-2018","24-08-2018","27-08-2018","28-08-2018"],
            ["16-08-2018","17-08-2018","20-08-2018","21-08-2018","22-08-2018","23-08-2018","24-08-2018","27-08-2018","28-08-2018","29-08-2018","30-08-2018","31-08-2018","03-09-2018","04-09-2018"],
            ["23-08-2018","24-08-2018","27-08-2018","28-08-2018","29-08-2018","30-08-2018","31-08-2018","03-09-2018","04-09-2018","05-09-2018","06-09-2018","07-09-2018","10-09-2018","11-09-2018"],
            ["30-08-2018","31-08-2018","03-09-2018","04-09-2018","05-09-2018","06-09-2018","07-09-2018","10-09-2018","11-09-2018","12-09-2018","13-09-2018","14-09-2018","17-09-2018","18-09-2018"]]
