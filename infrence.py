import pandas as pd 
# import yfinance as yf
import time
# import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
import yfinance as yf
# from keras.layers import Dense, LSTM
# import matplotlib.pyplot as plt
from Model.model import *

df = yf.download('^CRSLDX', start = '2024-01-01')
df.columns = ['_'.join(col).strip() for col in df.columns.values]
df.columns = [col.split('_')[0] for col in df.columns]
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

