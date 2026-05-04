import streamlit as st

st.title("Text Echo")

text = st.text_area("Write anything:")

if text:
    st.write(text)
