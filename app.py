import streamlit as st
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Title of the web app
st.title("🌸 Iris Flower Predictor")

# Input sliders
sepal_length = st.slider('Sepal Length (cm)', 4.0, 8.0, 5.1)
sepal_width = st.slider('Sepal Width (cm)', 2.0, 4.5, 3.5)
petal_length = st.slider('Petal Length (cm)', 1.0, 7.0, 1.4)
petal_width = st.slider('Petal Width (cm)', 0.1, 2.5, 0.2)

# Predict button
if st.button('Predict'):
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    flower_names = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f'The predicted flower is: {flower_names[result[0]]}')
