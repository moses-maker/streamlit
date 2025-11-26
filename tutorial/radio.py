import streamlit as st
color = st.radio(
    "What's your favorite Color", 
    [":rainbow[Rainbow]", "Black"],
    captions = ["All the colors in Rainbow", "Black rules"]
)
if color == ':rainbow[Rainbow]':
    st.write("You selected rainbow.")
else:
    st.write("You did not select rainbow")
