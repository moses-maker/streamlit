import streamlit as st
import sqlite3

# user database creation
conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                password TEXT UNIQUE
                )
          ''')

conn.commit()

# Functions to interact with DB
def register_user(name, password):
    c.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
    conn.commit()
    return True

def login_user(name, password):
    c.execute("SELECT * FROM users WHERE name = ? AND password = ?", (name, password))
    return c.fetchone()

st.title("WELCOME TO MARTIAL ARTS")
menu = st.sidebar.selectbox("Choose action", ["Login", "Register"])

if menu == "Register":
    st.subheader("Create New Account")
    new_user = st.text_input("Name", key="reg_name")
    new_password = st.text_input("Password", type='password', key="reg_pass")

    if st.button("Register"):
        if new_user and new_password:
            if register_user(new_user, new_password):
                st.success("Account created successfully! Go to Login.")
            else:
                st.error("Username already exists. Choose a different one.")
        else:
            st.warning("Please fill all fields.")

elif menu == "Login":
    st.subheader("Login to Your Account")

    username = st.text_input("Name", key="login_name")
    password = st.text_input("Password", type='password', key="login_pass")

    if st.button("Login"):
        if login_user(username, password):
            st.success(f"Welcome {username}!")

        else:
            st.error("Invalid credentials. Please try again.")

