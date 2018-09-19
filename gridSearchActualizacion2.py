def gridSearch(activations,neurons,learning_rate,epochs,random_seed,current,fecha7DiasSiguientes):
    activationUsed=[]
    neuronsUsed=[]
    learning_rateUsed=[]
    epochsUsed=[]
    random_seedUsed=[]
    errorUsed=[]
    predictionObtained=[]

    for a in activations:
        for b in neurons:
            for c in learning_rate:
                for d in epochs:
                    for e in random_seed:
                        m=TFModel(batch_size=14,lengthTasa=8,f_horizon=14,overlapSize=7,random_seed=e,neurons=b,activation=a,learning_rate=c,epochs=d,current=current)
                        p,e=m.plotPrediction(fecha7DiasSiguientes)
                        print("el error es:")
                        print(e)
                        errorUsed.append(e)
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
                    
    d={'prediction':predictionObtained,'neurons':neuronsUsed,'activation':activationUsed,'epochs':epochsUsed,'random_seed':random_seedUsed,'error':errorUsed,'learning_rate':learning_rateUsed}
    parametros=pd.DataFrame(d)
    parameters=parametros.sort_values(['error']).reset_index()
    return parameters
