import pandas as pd 
import numpy as np
import yfinance as yf


from Model.model import *
time_step =60

ticker_symbol = '^CRSLDX'
Start_Date = '2024-01-01'

# Get historical market data for nifty500
def load_df(Ticker_Symbol, Start):
    df = yf.download(Ticker_Symbol, Start)
    df.columns = ['_'.join(col).strip() for col in df.columns.values]
    df.columns = [col.split('_')[0] for col in df.columns]
    # Loading Data and formatting data.
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()
    df = df.reset_index()['close']
    #getting Nifty500 latest close value 
    df1 = pd.DataFrame(df).to_numpy()
    actual_value =df1[-1][0]
    return df, actual_value

def Nifty_Pred(Nifty500_Model):
    df, actual_value = load_df(ticker_symbol, Start_Date)
    predicted_value = Pred(df, time_step, Nifty500_Model)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(actual_value,predicted_value)
    return {"Predicted_Value": predicted_value, "Actual_Value": actual_value, "error": err}





