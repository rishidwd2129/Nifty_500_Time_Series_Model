import numpy as np
import pandas as pd
import yfinance as yf
from Model.model import *
from fastapi import FastAPI
from Nifty500 import *

#initialising time series batch for prediction
time_step =60
# Model Paths
Nifty500_Model = 'Model/lstm_model.h5'
Axis_Model = 'Model/AxisBK_Pred_model.h5'
Hdfc_Model = 'Model/HDFCBK_Pred_model.h5'
Icici_Model = 'Model/Icici_Pred_model.h5'
Infy_Model = 'Model/Infosys_Pred_model.h5'
Airtel_Model  = 'Model/Airtel_Pred_model.h5'
LnT_Model = 'Model/LT_Pred_model.h5'

#Ticker Symbols
ticker_symbols = ['AXISBANK.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'INFY.NS', 'BHARTIARTL.NS', 'LT.NS']

# Starting Date
Start_Date = '2024-01-01'
# Data Loading Function
def Load_df(Ticker_Symbol, Start):
    df = yf.download(Ticker_Symbol, Start)
    df.columns = ['_'.join(col).strip() for col in df.columns.values]
    df.columns = [col.split('_')[0] for col in df.columns]
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()
    df = df.reset_index()['close']
    df1 = pd.DataFrame(df).to_numpy()
    actual_value =df1[-1][0]
    return df,actual_value


# API hosting
app = FastAPI()

@app.get("/")
def Nifty500():
    result = Nifty_Pred(Nifty500_Model)
    return result

@app.get("/axis/")
def Axis_Prediction():
    df,actual_value = Load_df(ticker_symbols[0], Start_Date)
    predicted_value = Pred(df, time_step, Axis_Model)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(actual_value,predicted_value)
    return {"Predicted_Axis_Value": predicted_value, "Actual_Axis_Value": actual_value, "axis_error": err}

@app.get("/hdfc/")
def HDFC_Prediction():
    df, actual_value = Load_df(ticker_symbols[1], Start_Date)
    predicted_value = Pred(df, time_step, Hdfc_Model)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err (actual_value,predicted_value)
    return {"Predicted_HDFC_Value": predicted_value, "Actual_HDFC_Value": actual_value, "hdfc_error": err}

@app.get("/icici/")
def Icici_Prediction():
    df, actual_value = Load_df(ticker_symbols[2], Start_Date)
    predicted_value = Pred(df, time_step, Icici_Model)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(actual_value,predicted_value)
    return {"Predicted_Icici_Value": predicted_value, "Actual_Icici_Value": actual_value, "icici_error": err}

@app.get("/infy/")
def infyi_prediction():
    df, actual_value = Load_df(ticker_symbols[3], Start_Date)
    predicted_value = Pred(df, time_step, Infy_Model)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(actual_value,predicted_value)
    return {"Predicted_Infy_Value": predicted_value, "Actual_Infy_Value": actual_value, "infy_error": err}

@app.get("/airtel/")
def airtel_prediction():
    df, actual_value = Load_df(ticker_symbols[4], Start_Date)
    predicted_value = Pred(df, time_step, Airtel_Model)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(actual_value,predicted_value)
    return {"Predicted_Airtel_Value": predicted_value, "Actual_Airtel_Value": actual_value, "airtel_error": err}

@app.get("/LT/")
def LT_Prediction():
    df, actual_value = Load_df(ticker_symbols[5], Start_Date)
    predicted_value = Pred(df, time_step, LnT_Model)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(actual_value,predicted_value)
    return {"Predicted_LT_Value": predicted_value, "Actual_LT_Value": actual_value, "lt_error": err}