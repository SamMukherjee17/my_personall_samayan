import streamlit as st
import requests

st.title("Super Kart Sales Prediction")
# Input fields for product and store data
Product_Id_char  = st.selectbox("Product Id char ", ['FD', 'NC', 'DR'])
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.0)
Product_Category = st.selectbox("Product Category", ["Perishable", "Non_Perishable"])
Product_MRP = st.number_input("Product MRP", min_value=0.0)
Store_Id = st.selectbox("Store Id", ['OUT001', 'OUT002', 'OUT003', 'OUT004'])
Store_Size = st.selectbox("Store Size", ["Small", "Medium", "High"])
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
Store_Type = st.selectbox("Store Type", ["Supermarket Type2", "Departmental Store","Supermarket Type1","Food Mart"])
store_age = st.number_input("Store Age", min_value=0.0)

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Id": Store_Id,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "store_age": store_age,
    "Product_Category": Product_Category
}

# Create a button to trigger the prediction
if st.button("Predict"):
  # Sending request to the backend container (assuming Docker Compose deployment)
  try:
      response = requests.post("http://backend:5000/v1/predict", json=product_data)
      response.raise_for_status()
      prediction = response.json().get('predicted_sales')
      st.success(f"Predicted Sales: {prediction:.2f}")
  except Exception as e:
      st.error(f"Error connecting to backend: {e}")
