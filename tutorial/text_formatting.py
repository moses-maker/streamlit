import streamlit as st

st.title("STREAMLIT TITLE")
st.header("This is a header")
st.subheader("This is a subheader")

# text 
st.write("Hello world")
st.text("Th is some text")

# user input
st.text_input("Enter name", "Type here...")
st.text_area("Enter your message:", "Type here...")

# Numbers
st.number_input("Enter number", min_value=10, max_value=100)

# Date
st.date_input("Enter date") 
st.time_input("Enter time")

# camera
st.camera_input("Take a picture:")

