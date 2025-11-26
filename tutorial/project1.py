import streamlit as st
import sqlite3

# create a database
connection = sqlite3.connect("Phone.db")
c = connection.cursor()

# create a table
def create_table():
    c.execute('''
            CREATE TABLE IF NOT EXISTS contacts(
            admission INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            mobile TEXT NOT NULL
            )
    ''')
    connection.commit()

def add_data(admission, name, mobile):
    c.execute("INSERT INTO contacts (admission, name, mobile) VALUES(?,?,?)", (admission, name, mobile))
    connection.commit()

def view_data():
    c.execute("SELECT * FROM contacts")
    return c.fetchall()

def main():
    st.title("Contact Book")
    menu = ["Add", "View"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()

    if choice == "Add":
        st.subheader("Add New Entry")
        admission = st.number_input("Enter your admission number?")
        name = st.text_input("Enter your name?")
        mobile = st.text_input("Enter your mobile number?")

        if st.button("Save"):
            add_data(admission, name, mobile)
            st.success(f"Data for {name} saved successfully")

    if choice=="View":
        st.subheader("View Records")
        data = view_data()
        for row in data:
            st.write(f"Admission {row[0]}, Name {row[1]}, Mobile {row[2]}")

if __name__ == "__main__":
    main()
