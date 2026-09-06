from ast import main

import streamlit as st
from db_helper import create_table


def main():
    create_table()
    st.title("Student Login System")
    choice = st.sidebar.selectbox("Select an option", ["Login", "Register"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    st.button("login")
    


if __name__ == "__main__":
    main()