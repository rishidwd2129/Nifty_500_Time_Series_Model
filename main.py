
import multiprocessing
import numpy as np
import pandas as pd
import yfinance as yf
import multiprocessing
from Model.model import *
from fastapi import FastAPI
from Nifty500 import *

# dotenv_path = ".env/.env"
# load_dotenv(dotenv_path)
# # Access the API token
# key = os.getenv('API')
# # Access the API token
# key = os.getenv('API')
time_step =60

# Get historical market data for nifty500
# df = yf.download('^CRSLDX', start = '2024-01-01')
# df.columns = ['_'.join(col).strip() for col in df.columns.values]
# df.columns = [col.split('_')[0] for col in df.columns]
# # Loading Data and formatting data.
# df.columns = df.columns.str.strip()
# df.columns = df.columns.str.lower()
# df = df.reset_index()['close']
# #getting Nifty500 latest close value 
# df1 = pd.DataFrame(df).to_numpy()
# actual_value =df1[-1][0]

# nifty500 ends here 
#starting Axis data laod and formatting

def load_axis():
    global Axis_actual_value
    Axis_df =yf.download('AXISBANK.NS', start = '2024-01-01')
    Axis_df.columns = ['_'.join(col).strip() for col in Axis_df.columns.values]
    Axis_df.columns = [col.split('_')[0] for col in Axis_df.columns]
    Axis_df.columns = Axis_df.columns.str.strip()
    Axis_df.columns = Axis_df.columns.str.lower()
    Axis_df = Axis_df.reset_index()['close']
    Axis_df1 = pd.DataFrame(Axis_df).to_numpy()
    Axis_actual_value =Axis_df1[-1][0]

#Axis Ends here

# HDFC Data laoding and formatting
def load_hdfc():
    global hdfc_actual_value
    hdfc_df = yf.download('HDFCBANK.NS', start = '2024-01-01')
    hdfc_df.columns = ['_'.join(col).strip() for col in hdfc_df.columns.values]
    hdfc_df.columns = [col.split('_')[0] for col in hdfc_df.columns]
    hdfc_df.columns = hdfc_df.columns.str.strip()
    hdfc_df.columns = hdfc_df.columns.str.lower()
    hdfc_df = hdfc_df.reset_index()['close']
    hdfc_df1 = pd.DataFrame(hdfc_df).to_numpy()
    hdfc_actual_value = hdfc_df1[-1][0]
#HDFC ends here

# L&T dtaa loading and formatting
LnT_df = yf.download('LT.NS', start = '2024-01-01')
LnT_df.columns = ['_'.join(col).strip() for col in LnT_df.columns.values]
LnT_df.columns = [col.split('_')[0] for col in LnT_df.columns]
LnT_df.columns = LnT_df.columns.str.strip()
LnT_df.columns = LnT_df.columns.str.lower()
LnT_df = LnT_df.reset_index()['close']
LnT_df1 = pd.DataFrame(LnT_df).to_numpy()
LnT_actual_value = LnT_df1[-1][0]

# L&T Ends here

#ICICI data laoding and formatting 
Icici_df = yf.download('ICICIBANK.NS', start = '2024-01-01')
Icici_df.columns = ['_'.join(col).strip() for col in Icici_df.columns.values]
Icici_df.columns = [col.split('_')[0] for col in Icici_df.columns]
Icici_df.columns = Icici_df.columns.str.strip()
Icici_df.columns = Icici_df.columns.str.lower()
Icici_df = Icici_df.reset_index()['close']
Icici_df1 = pd.DataFrame(Icici_df).to_numpy()
Icici_actual_value = Icici_df1[-1][0]

# ICICI ends here

# Infosys data loading and formatting
Infy_df = df = yf.download('INFY.NS', start = '2024-01-01')
Infy_df.columns = ['_'.join(col).strip() for col in Infy_df.columns.values]
Infy_df.columns = [col.split('_')[0] for col in Infy_df.columns]
Infy_df.columns = Infy_df.columns.str.strip()
Infy_df.columns = Infy_df.columns.str.lower()
Infy_df = Infy_df.reset_index()['close']
Infy_df1 = pd.DataFrame(Infy_df).to_numpy()
Infy_actual_value = Infy_df1[-1][0]

# Infosys ends here

# Airtel dataloading and formatting
Airtel_df = yf.download('BHARTIARTL.NS', start = '2024-01-01')
Airtel_df.columns = ['_'.join(col).strip() for col in Airtel_df.columns.values]
Airtel_df.columns = [col.split('_')[0] for col in Airtel_df.columns]
Airtel_df.columns = Airtel_df.columns.str.strip()
Airtel_df.columns = Airtel_df.columns.str.lower()
Airtel_df = Airtel_df.reset_index()['close']
Airtel_df1 = pd.DataFrame(Airtel_df).to_numpy()
Airtel_actual_value = Airtel_df1[-1][0]

# airtel ends here
if __name__ == "__main__":
    # creating processes
    p_axis = multiprocessing.process(target = load_axis)
    p_hdfc = multiprocessing.process(target = load_hdfc)
    p_nifty500 = multiprocessing.process(target = load_nifty_500)
    # p1 = multiprocessing.Process(target=print_square, args=(10, ))
    # p2 = multiprocessing.Process(target=print_cube, args=(10, ))

    # starting process 1
    p_axis.start()
    # starting process 2
    p_hdfc.start()
    
    p_nifty500.start()
    
    p_nifty500.join()
    p_axis.join()
    p_hdfc.join()


# API hosting
app = FastAPI()

@app.get("/")
def Nifty500():
    # predicted_value = predict(df, time_step)
    # predicted_value = predicted_value[0][0]
    # predicted_value = float(predicted_value)
    # print(predicted_value)
    # err = cal_err(actual_value,predicted_value)
    result = Nifty_Pred()
    # return {"Predicted_Value": predicted_value, "Actual_Value": actual_value, "error": err}
    return result

@app.get("/axis/")
def Axis_Prediction():
    predicted_value = Axis_Pred(Axis_df, time_step)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(Axis_actual_value,predicted_value)
    return {"Predicted_Axis_Value": predicted_value, "Actual_Axis_Value": Axis_actual_value, "axis_error": err}

@app.get("/hdfc/")
def HDFC_Prediction():
    predicted_value = HDFC_Pred(hdfc_df, time_step)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(hdfc_actual_value,predicted_value)
    return {"Predicted_HDFC_Value": predicted_value, "Actual_HDFC_Value": hdfc_actual_value, "hdfc_error": err}

@app.get("/LT/")
def LT_Prediction():
    predicted_value = LT_Pred(LnT_df, time_step)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(LnT_actual_value,predicted_value)
    return {"Predicted_LT_Value": predicted_value, "Actual_LT_Value": LnT_actual_value, "lt_error": err}

@app.get("/icici/")
def Icici_Prediction():
    predicted_value = Icici_Pred(Icici_df, time_step)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(Icici_actual_value,predicted_value)
    return {"Predicted_Icici_Value": predicted_value, "Actual_Icici_Value": Icici_actual_value, "icici_error": err}

@app.get("/infy/")
def infyi_prediction():
    predicted_value = Infy_Pred(Infy_df, time_step)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(Infy_actual_value,predicted_value)
    return {"Predicted_Infy_Value": predicted_value, "Actual_Infy_Value": Infy_actual_value, "infy_error": err}

@app.get("/airtel/")
def airtel_prediction():
    predicted_value = Airtel_Pred(Airtel_df, time_step)
    predicted_value = predicted_value[0][0]
    predicted_value = float(predicted_value)
    err = cal_err(Airtel_actual_value,predicted_value)
    return {"Predicted_Airtel_Value": predicted_value, "Actual_Airtel_Value": Airtel_actual_value, "airtel_error": err}