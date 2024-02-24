import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import webbrowser
import plotly.graph_objects as go


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="IOT", page_icon="", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
img_bg1_form = Image.open("images/monitoring.jpg")
lottie_coding2 = load_lottieurl("https://lottie.host/9eed2724-9ac9-42dd-81ef-cac66bfc1525/ZShaVGeP4I.json")

# ---- PROJECTS ----
with st.container():
    st.header("RECYCLE WASTE MONITORING AND NOTIFICATIONS")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_bg1_form)
    with text_column:
        st.subheader("Blynk Monitoring and Notification")
        st.write(
            """
            Monitoring and notification using Blynk Cloud allows for real-time tracking and alerting of various systems and devices. 
            With Blynk Cloud, users can remotely monitor sensor data, control actuators, and receive notifications on their web,smartphones,tablets. 
            It provides a user-friendly interface to visualize data, set thresholds, and trigger alerts based on predefined conditions. 
            Whether it's monitoring environmental parameters, home automation systems, or industrial processes, 
            Blynk Cloud empowers users to stay informed and take timely actions, ensuring efficiency, safety, and convenience.
            To see monitoring and notification click a button "GET BLYNK" below.
            """
        )
        if st.button("GET BLYNK"):
            webbrowser.open_new_tab("https://blynk.cloud/dashboard/login")
with st.container():
    image_column, text_column = st.columns((1, 2))

    with st.container():
        left_column, right_column = st.columns(2)
with left_column:
     st_lottie(lottie_coding2, height=250, key="coding2")

        

