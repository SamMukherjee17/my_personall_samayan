
# Import necessary libraries
import numpy as np
import joblib  # For loading the serialized model
import pandas as pd  # For data manipulation
from flask import Flask, request, jsonify  # For creating the Flask API

#Initialize flask app with name
super_kart_api = Flask("superkart")

# Load the saved model pipeline from the file
superkart_model = joblib.load('backend_files/superkart_pred.joblib')

#Define a route for the home page
@super_kart_api.get('/')
def home():
    return "Super Kart API"

#Define endpoint to predict single values
@super_kart_api.post('v1/predict')
def predict_sales():
  #Get json data
   data = request.get_json()

   # Check if data is not blank
   if not data:
       return jsonify({'error': 'No data provided'}), 400

   # Extract relevant customer features from the input data, ensuring correct naming and handling missing keys
   sample = {
        'Product_Weight': data.get('Product_Weight'),
        'Product_Sugar_Content': data.get('Product_Sugar_Content'),
        'Product_Allocated_Area': data.get('Product_Allocated_Area'),
        'Product_MRP': data.get('Product_MRP'),
        'Store_Id': data.get('Store_Id'),
        'Store_Size': data.get('Store_Size'),
        'Store_Location_City_Type': data.get('Store_Location_City_Type'),
        'Store_Type': data.get('Store_Type'),
        'Product_Id_char': data.get('Product_Id_char'),
        'store_age': data.get('store_age'),
        'Product_Category': data.get('Product_Category')
    }

   # Convert the sample dictionary to a pandas DataFrame
   # The model expects a DataFrame with the correct column order and names
   input_df = pd.DataFrame([sample])

   # Make prediction
   prediction = superkart_model.predict(input_df)[0] # [0] to get the scalar value

   # Return the prediction as JSON
   return jsonify({'predicted_sales': prediction})
