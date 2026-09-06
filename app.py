from ast import main

import streamlit as st
from db_helper import create_table,verify_user,fetch_user


def main():
    create_table()
st.title("Student Login System")

if __name__ == "__main__":
    main()