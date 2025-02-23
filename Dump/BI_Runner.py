import requests
import pandas as pd
# Define the URL of the FastAPI endpoint
url = 'http://localhost:8000'  # Replace with the actual URL if different

# Make a GET request to the endpoint for Nifty 500
response = requests.get(url)
data = response.json()
Predicted_value = data['Predicted_Value']
Actual_Value = data['Actual_Value']
err = data['error']
data = {
    'Predicted Value': [Predicted_value],
    'Actual Value': [Actual_Value],
    'Error': [err]
}
df = pd.DataFrame(data)

# get resposne for Axis 

axis_url = 'http://localhost:8000/axis/'
axis_response = requests.get(axis_url)
axis_data = axis_response.json()
Axis_Predicted_Value = axis_data["Predicted_Axis_Value"]
Axis_Actual_Value = axis_data["Actual_Axis_Value"]
Axis_err = axis_data["axis_error"]
data = {
    'Axis_Predicted_Value': Axis_Predicted_Value,
    'Axis_Actual_Value': Axis_Actual_Value,
    'Axis_Error': Axis_err
}

Axis_df = pd.DataFrame(data)
print(Axis_df)
# Get hdfc response

hdfc_url = 'http://localhost:8000/hdfc/'

hdfc_response = requests.get(hdfc_url)
hdfc_data = hdfc_response.json()
Hdfc_Predicted_Value = hdfc_data["Predicted_HDFC_Value"]
Hdfc_Actual_Value = hdfc_data["Actual_HDFC_Value"]
Hdfc_err = hdfc_data["hdfc_error"]
data = {
    'HDFC_Predicted_Value': Hdfc_Predicted_Value,
    'HDFC_Actual_Value': Hdfc_Actual_Value,
    'HDFC_Error': Hdfc_err
}
HDFC_df = pd.DataFrame(data)
print(HDFC_df)

# Get L&T response

LnT_url = 'http://localhost:8000/LT/'
LnT_response = requests.get(LnT_url)
LnT_data = LnT_response.json()
LnT_Predicted_Value = LnT_data["Predicted_LT_Value"]
LnT_Actual_Value = LnT_data["Actual_LT_Value"]
LnT_err = LnT_data["lt_error"]
data = {
    'LT_Predicted_Value': LnT_Predicted_Value,
    'LT_Actual_Value': LnT_Actual_Value,
    'LT_Error': LnT_err
}
LnT_df = pd.DataFrame(data)
print(LnT_df)

# Get ICICI response

ICICI_url = 'http://localhost:8000/icici/'
ICICI_response = requests.get(ICICI_url)
ICICI_data = ICICI_response.json()
ICICI_Predicted_Value = ICICI_data["Predicted_Icici_Value"]
ICICI_Actual_Value = ICICI_data["Actual_Icici_Value"]
ICICI_err = ICICI_data["icici_error"]

data = {
    'ICICI_Predicted_Value': ICICI_Predicted_Value,
    'ICICI_Actual_Value': ICICI_Actual_Value,
    'ICICI_Error': ICICI_err
}

ICICI_df = pd.DataFrame(data)

print(ICICI_df)

#  get Infosys response

Infy_url = 'http://localhost:8000/infy/'

Infy_response = requests.get(Infy_url)
Infy_data = Infy_response.json()
Infy_Predicted_Value = Infy_data["Predicted_Infy_Value"]
Infy_Actual_Value = Infy_data["Actual_Infy_Value"]
Infy_err = Infy_data["infy_error"]
data = {
    'Infosys_Predicted_Value': [Infy_Predicted_Value],
    'Infosys_Actual_Value' : [Infy_Actual_Value],
    'Infosys_Error' : [Infy_err]
}
Infy_df = pd.DataFrame(data)
print(Infy_df)



# get Airtel response

Airtel_url = 'http://localhost:8000/airtel/'
Airtel_response = requests.get(Airtel_url)
Airtel_data = Airtel_response.json()
Airtel_Predicted_Value = Airtel_data["Predicted_Airtel_Value"]
Airtel_Actual_Value = Airtel_data["Actual_Airtel_Value"]
Airtel_err = Airtel_data["airtel_error"]

data = {
    'Airtel_Predicted_Value': Airtel_Predicted_Value,
    'Airtel_Actual_Value': Airtel_Actual_Value,
    'Airtel_Error': Airtel_err
}