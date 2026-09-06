import streamlit as st
st.title("login page")
class login:
    status = "active"
    def __init__(self, username,password,mark):
        self.username = username
        self.password = password
        self.mark = mark 

    def get_total(self):
        return sum(self.mark)

result = login("samuel","samuel123",{48,96,80,86,97})
print(result.username)
print(result.password)
print("total mark",result.get_total())