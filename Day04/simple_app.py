import streamlit as st
st.title("☘️ Plantery ")
st.header("Behold , My Fellow Greenlings ")
st.subheader("Welcome to the world of photosynthesis 🪸 and chlorophyll 🦠")
name=st.text_input("Enter your evergreen name : ")
if st.button("Submit"):
    st.write("Hello",name)
st.badge("🌿")

