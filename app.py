import streamlit as st
import joblib

model = joblib.load('model.pkl')

st.title("🌸 Iris Flower Predictor")

sepal_length = st.slider('Sepal Length', 4.0, 8.0)
sepal_width = st.slider('Sepal Width', 2.0, 4.5)
petal_length = st.slider('Petal Length', 1.0, 7.0)
petal_width = st.slider('Petal Width', 0.1, 2.5)

if st.button('Predict'):
result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
st.success(f'The predicted flower is: {result[0]}')