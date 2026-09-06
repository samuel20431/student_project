import streamlit as st
st.title("login page")
class login:
    status = "active"
    def __init__(self, username,password):
        self.username = username
        self.password = password
         

    def get_total(self):
        return sum(self.mark)

result = login("samuel","samuel123")
print(result.username)
print(result.password)
