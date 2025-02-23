import numpy as np
from numpy import array
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model




def Pred(df, time_step, Model):# input arguments dataframe, time step, Model path
    scaler=MinMaxScaler (feature_range=(0,1))
    df=scaler.fit_transform(np.array(df).reshape(-1,1))
    x_input = df[-62:-2].reshape(1,-1)
    temp_input = list(x_input)
    temp_input = temp_input[0].tolist()
    model = load_model(Model)
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
            # print(yhat[0])
            temp_input.extend(yhat[0].tolist())
            # print(len(temp_input))
            lst_output.extend(yhat.tolist())
            i=i+1
    yhat=scaler.inverse_transform(yhat)
    return yhat

def cal_err(actual_value,predicted_value):
    err = (predicted_value - actual_value)/actual_value
    err = err*100

    return err
    

