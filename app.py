from ast import main

import streamlit as st
from db_helper import create_table, add_student


def main():
    create_table()
    st.title("Student Login System")
    choice = st.sidebar.selectbox("Select an option", ["Login", "Register"])
    if choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
    elif choice == "Register":
        st.subheader("Register")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")    
        if st.button("Register"):
            add_student(username, password)
            st.success("You have successfully registered!")
        else:
            st.warning("username already exists. Please choose a different username.")


if __name__ == "__main__":
    main()