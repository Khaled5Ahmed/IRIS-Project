from controller.LoadModel import LoadModel
from controller.GetPrediction import GetPrediction
import streamlit as st 

st.title("Iris Flower Prediction App")
st.write("Enter the characteristics of the iris flower : ")

sepal_lenght = st.number_input("Sepal Lenght(cm)" , min_value = 0.0 , max_value = 10.0 , step = 0.1) 
sepal_width = st.number_input("Sepal Width(cm)" , min_value = 0.0 , max_value = 10.0 , step = 0.1)
petal_lenght = st.number_input("Petal Lenght(cm)" , min_value = 0.0 , max_value = 10.0 , step = 0.1)
petal_width =st.number_input("Petal Width(cm)" , min_value = 0.0 , max_value = 10.0 , step = 0.1)

model=LoadModel("Iris_model.pkl")

if st.button("predict"):
    predection = GetPrediction(model,[sepal_lenght,sepal_width,petal_lenght,petal_width])
    
    st.write(f"The predicted class of the iris flower is : {predection}")