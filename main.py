import streamlit as st
from pytubefix import YouTube
import socket


st.title("Streamlit Testing")
st.write("This is my streamlit testing app for development purposes.")

#Getting IP address

def GetIP():
    host = socket.gethostname()
    IPaddr = socket.gethostbyname(host)
    st.write(f"Your IP Address is: {IPaddr}")
    return 

def GetVideo(url):
    yt = YouTube(url=url)
    best = yt.streams.get_highest_resolution()
    best.download()






st.button("Get IP", on_click=GetIP)


st.header("Testing pytubefix")





with st.form("Youtube Download"):
    st.write("Super simple video download test")
    url = st.text_input(label="Input URL")
    submitted = st.form_submit_button(label="Submit")
    if submitted:
        GetVideo(url)