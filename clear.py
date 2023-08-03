
import streamlit as st

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:")

if st.form_submit_button(label='Clear'):
    name = ""
    age = ""