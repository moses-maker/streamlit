import streamlit as st

# single input select
agree = st.checkbox("I agree")

# Checkbox returns true/false
if agree:
    st.write("You have agreed")

# horizontal line
st.divider()

on = st.toggle("Activate feature")
if on:
    st.write("Feature activated")

volume = st.slider("Adjust the volume?", 0, 130, 10)
st.write("The new volume is", volume)


