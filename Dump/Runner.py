import pandas as pd 
# import yfinance as yf
import time
# import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
import numpy as np
from numpy import array
from sklearn.preprocessing import MinMaxScaler
# from keras.models import Sequential
from keras.models import load_model
# from keras.layers import Dense, LSTM
# import matplotlib.pyplot as plt
# from Model.model import *

#  Functions 
def predict(df, time_step):
    df=scaler.fit_transform(np.array(df).reshape(-1,1))
    x_input = df[-62:-2].reshape(1,-1)
    temp_input = list(x_input)
    temp_input = temp_input[0].tolist()
    import os
    dir = os.getcwd()

    
    model = load_model('Model/lstm_model.h5')
    
    lst_output=[]
    n_steps=time_step
    i=0
    while(i<1):

        if(len(temp_input)>time_step):
            #print(temp_input)
            x_input=np.array(temp_input[1:])
            print("{} day input {}".format(i,x_input))
            x_input=x_input.reshape(1,-1)
            x_input = x_input.reshape((1, n_steps, 1))
            #print(x_input)
            yhat = model.predict(x_input, verbose=0)
            print("{} day output {}".format(i,yhat))
            temp_input.extend(yhat[0].tolist())
            temp_input=temp_input[1:]
            #print(temp_input)
            lst_output.extend(yhat.tolist())
            i=i+1
        else:
            x_input = x_input.reshape((1, n_steps,1))
            yhat = model.predict(x_input, verbose=0)
            print(yhat[0])
            temp_input.extend(yhat[0].tolist())
            print(len(temp_input))
            lst_output.extend(yhat.tolist())
            i=i+1
    yhat=scaler.inverse_transform(yhat)
    return yhat

def cal_err(actual_value,predicted_value):
    err = (predicted_value - actual_value)/actual_value
    err = err*100
    return err

# Function Ends

# Executing Prediction



df = pd.read_csv('Data.csv')
df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()
df = df.reset_index()['close']
df1 = pd.DataFrame(df).to_numpy()
actual_value =df1[-1][0]
time_step =60




predicted_value = predict(df, time_step)
predicted_value = predicted_value[0][0]

err = cal_err(actual_value,predicted_value)

print(f"Actual Vaule,{actual_value}")
print(f'Predicted Value: {predicted_value}')
print('------------------------------------------------------------')
print(f'error: {err}')

