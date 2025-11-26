import streamlit as st

st.button("Reset", type="primary")

if st.button("Say Good morning"):
    st.write("Good evening")