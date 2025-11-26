import streamlit as st
import sqlite3

# Create a database
connection = sqlite3.connect("student.db")
cursor = connection.cursor()


# Create a records table
def Create_Table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Records(
    Adm INTEGER PRIMARY KEY,
    Stdname TEXT NOT NULL,
    Maths INTEGER NOT NULL,
    Eng INTEGER NOT NULL,
    Ksw INTEGER NOT NULL,
    Sci INTEGER NOT NULL
     )
    ''')
    connection.commit()

# Adds data to the table
def Add_Data(Adm, Stdname, Maths, Eng, Ksw, Sci):
    cursor.execute("INSERT INTO Records(Adm, Stdname, Maths, Eng, Ksw, Sci) VALUES(?,?,?,?,?, ?)", (Adm, Stdname, Maths, Eng, Ksw, Sci))
    connection.commit()

# View data from the database
def View_Data():
    cursor.execute("SELECT * FROM Records")
    return cursor.fetchall()

# the main function
def main():
    st.title("STUDENT MARKS ENTRY FORM")
    menu = ["Add Student Marks", "View Student Marks"]
    st.sidebar.header("Choices Menu")
    choice = st.sidebar.selectbox("Menu", menu)
    # Call create_table() function to create the table records
    Create_Table()

    if choice == "Add Student Marks":
        st.subheader("Add a Student Marks")
        Adm = st.number_input("Enter the admission number?")
        Stdname = st.text_input("Enter the student name?")
        Maths = st.number_input("Enter marks for Mathematics?")
        Eng = st.number_input("Enter marks for English?")
        Ksw = st.number_input("Enter marks for Kiswahili?")
        Sci = st.number_input("Enter marks for Science?")

        if st.button("Save"):
            Add_Data(Adm, Stdname, Maths, Eng, Ksw, Sci)
            st.success(f"Data for {Stdname} saved successfully")

    if choice == "View Student Marks":
        st.subheader("View The Marks for Student")
        all_records = View_Data()
        headers = ["Admission", "Mathematics", "English", "Kiswahili", "Science"]

        st.write(tabulate(all_records, headers=headers, tablefmt="grid"))
        connection.close()

if __name__  == "__main__":
    main()
