import streamlit as st
import sklearn
import joblib
model = joblib.load('Movie Review Sentiment')
st.title('Movie Sentiment')
ip = st.text_input('Enter your review')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
