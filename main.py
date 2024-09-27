import streamlit as st
from pytubefix import YouTube
import socket
from streamlit.components.v1 import html

st.title("Streamlit Testing")
st.write("This is my streamlit testing app for development purposes.")

#Getting IP address

def GetIP():
    host = socket.gethostname()
    IPaddr = socket.gethostbyname(host)
    st.write(f"Your IP Address is: {IPaddr}")
    return 

def GetVideo(url):
    try:
        yt = YouTube(url=url, use_po_token=True, token_file="Mytokens.txt")
        best = yt.streams.get_highest_resolution()
        best.download()
        global Completed
        Completed = True
        global video_bytes
        try:
            with open(yt.title+".mp4", "rb") as file:
                video_bytes = file.read()  # Read the binary content of the file
        except FileNotFoundError:
            st.error("The specified file was not found.")
            video_bytes = None
        st.write("Download complete")
    except Exception as e:
        st.write(f"Error Occurred:{e}")



Completed = False

st.button("Get IP", on_click=GetIP)


st.header("Testing pytubefix")





with st.form("Youtube Download"):
    st.write("Super simple video download test")
    url = st.text_input(label="Input URL")
    submitted = st.form_submit_button(label="Submit")
    if submitted:
        GetVideo(url)


if Completed:
    st.download_button(data=video_bytes, label="Download Video", mime="video/mp4")

# JS test

my_js = """
alert("hello")
"""

my_html = f"<script>{my_js}</script>"

#html(my_html)