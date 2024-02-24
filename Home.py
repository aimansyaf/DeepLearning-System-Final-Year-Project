import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


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
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_coding1 = load_lottieurl("https://lottie.host/c8e0c266-7b57-4c1e-b835-9d7e3bd10f5a/ucDkkktqDw.json")
lottie_coding2 = load_lottieurl("https://lottie.host/b3edd7c6-71ac-4e37-b9c4-a14c1caf724f/tiNssyZ48i.json")

img_contact_form = Image.open("images/yt_contact_form.png")
img_gambar_form = Image.open("images/yt_gambar_form.png")
img_bg1_form = Image.open("images/yt_bg1_form.png")

# ---- HEADER SECTION ----
with st.container():
    st.title("REAL TIME INTELLIGENT RECYCLE WASTE DETECTION AND CLASSIFICATION USING YOU ONLY LOOK ONCE VERSION 5")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container():
            img_plastic_form = Image.open("images/plastic_form.png")
            st.image(img_plastic_form, width=400)  # Set the width of the image
            st.subheader("Plastic")
            st.write("Plastic waste can have a significant impact on the environment. By recycling plastic, we can reduce pollution and conserve resources.")
    with col2:
        with st.container():
            img_metal = Image.open("images/metal.png")
            st.image(img_metal, width=400)  # Set the width of the image
            st.subheader("Metal")
            st.write("Recycling metal is important as it helps reduce the need for mining, conserves energy, and minimizes greenhouse gas emissions.")
    with col3:
        with st.container():
            img_paper = Image.open("images/paper.png")
            st.image(img_paper, width=400)  # Set the width of the image
            st.subheader("Paper")
            st.write("Recycling paper saves trees, reduces water and energy consumption, and lowers greenhouse gas emissions. It's an eco-friendly choice.")

# Rest of the code...



# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Below give are the objects the our model will detect:
            1. Metal
            2. Plastic
            3. Paper
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Recycle Waste Images")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_bg1_form)
    with text_column:
        st.subheader("Recycle the present, save the future.")
        st.write(
            """
            Recycling is more than just a response to the environmental crisis and has assumed a symbolic role in beginning 
            to change the nature of western societies and the culture of consumerism. Indeed many environmentalists assume 
            that there will be an inevitable shift from our "throwaway" society to a post-industrial "recycling" society of the future.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_gambar_form)
    with text_column:
        st.subheader("Recycle today for a better tomorrow.")
        st.write(
            """
            While recycling is great in a lot of ways, the ultimate goal is to get people to prevent waste in the first place.’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    


    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/aimansyafwan@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_coding1, height=350, key="coding1")

        