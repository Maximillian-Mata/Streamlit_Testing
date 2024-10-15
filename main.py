import streamlit as st
from pytubefix import YouTube
import socket
from streamlit.components.v1 import html
import execjs
# node usage
import subprocess

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
        st.write("Download complete")
    except Exception as e:
        st.write(f"Error Occurred:{e}")


def GetValid():
    my_js = """
        const { generate } = require('youtube-po-token-generator')

        let visitor;
        let po;

        function Collect(items){
            visitor = items.visitorData;
            po = items.poToken;
        }

        generate().then(Collect, console.err)

        """
    ctx = execjs.compile(my_js)
    ctx.call("generate")

    return 



st.button("Get IP", on_click=GetIP)
get_token = st.button("Update Po")
if get_token:
    output = subprocess.run(['node', "poget.js"], capture_output=True, text=True)
    st.write(str(output))


st.header("Testing pytubefix")





with st.form("Youtube Download"):
    st.write("Super simple video download test")
    url = st.text_input(label="Input URL")
    submitted = st.form_submit_button(label="Submit")
    if submitted:
        GetVideo(url)

#st.button(label="get number", on_click=GetValid)
