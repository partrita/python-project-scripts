import joblib
import numpy as np


def label_encoder(x):
    if x == 'M':
        return 1
    elif x == 'E':
        return 2
    elif x == 'E+':
        return 3
    elif x == 'S':
        return 4
    
    
def process_and_predict(data):
    #process the data
    data = (np.array(data)).reshape(1, -1)
    
    #load the model
    model = joblib.load('model')
    
    #model prediction
    prediction = next(iter(model.predict(data)))
    
    if prediction == 0:
        text = "Not Eligible"
    elif prediction == 1:
        text = "Eligible"
    
    return text
