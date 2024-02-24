import streamlit as st

st.markdown("<h1 style='text-align: center; color: black; padding: 0rem;'>Instruction</h1>", unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.markdown("<h4 style='text-align: center; color: black; padding: 0rem;'>YOLO FOR IMAGES</h4>", unsafe_allow_html=True)

    with st.container():
        st.write("---")
        st.markdown('<div style="text-align: center;">1. Maximum upload 200 MB per file</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: center;">2. Only accept png or jpg image</div>', unsafe_allow_html=True)

        with st.container():
            st.write("---")
            st.markdown("<h4 style='text-align: center; color: black; padding: 0rem;'>YOLO FOR REAL TIME VIDEOS</h4>", unsafe_allow_html=True)
            with st.container():
                st.write("---")
                st.markdown('<div style="text-align: center;">1. Click the real time YOLO and select the type of video input and audio input</div>', unsafe_allow_html=True)



        
