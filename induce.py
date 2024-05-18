import joblib
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler, MinMaxScaler


def Induce(record:np.array, modelList:list, combiner='combiner', scaler='minMax'):

    if record.ndim == 1:
        
        record = record.reshape(1, -1)

    scaler = joblib.load('model/{}.pkl'.format(scaler))

    record = scaler.transform(record)

    probabilityList = []

    for x in modelList + [combiner]:

        model = joblib.load('model/{}.pkl'.format(x))
        
        if x == combiner:
            
            probabilityList = np.array(probabilityList).reshape(1, -1)


            probability = model.predict_proba(probabilityList)[:, 1]


            probabilityList = np.concatenate([probabilityList.flatten(), probability])

        
        else:

            probability = model.predict_proba(record)[:, 1]

            probabilityList.append(probability)

    return probabilityList

if __name__ == "__main__":
    modelList = ['svm', 'rf', 'mlp', 'logistic', 'nb', 'dt', 'knn']
    rawDataset = pd.read_csv('diabetes.csv')
    record, label = rawDataset.values[0,:-1], rawDataset.values[0,-1]
    print(Induce(record, modelList))
    print(label)