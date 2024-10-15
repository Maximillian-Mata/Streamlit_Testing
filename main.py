import streamlit as st
from pytubefix import YouTube
import socket
#from streamlit.components.v1 import html
#import execjs
# node usage
import subprocess


def install_npm_package(package_name):
    try:
        # Run the npm install command using subprocess
        subprocess.run(['npm', 'install', package_name], capture_output=True, text=True, check=True)
        st.write(f"{package_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        st.write(f"Failed to install {package_name}: {e}")

#install_npm_package('youtube-po-token-generator')

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


st.button("Get IP", on_click=GetIP)
get_token = st.button("Update Po")
if get_token:
    output = subprocess.run(['node', "test.js"], capture_output=True, text=True)
    st.write(str(output))


st.header("Testing pytubefix")





with st.form("Youtube Download"):
    st.write("Super simple video download test")
    url = st.text_input(label="Input URL")
    submitted = st.form_submit_button(label="Submit")
    if submitted:
        GetVideo(url)

#st.button(label="get number", on_click=GetValid)
