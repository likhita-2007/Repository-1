import ollama
import streamlit as st

st.title(":blue[☘️ Vrikshavan] ")
st.divider()
st.header("*Behold , My Fellow Greenlings 🌱*")
st.subheader("_Welcome to the world of photosynthesis 🪸 and chlorophyll 🦠_")

with st.sidebar:
    st.title("Chat Settings")

    personalities={
        "Kid":"Give answers like you are explaining to a 5 year old kid. Give the answer in 3 lines only.",
        "Professor":"You are an Oxford professor. Explain the topic using correct terminologies. Give the answer in 3 lines only. "
}
    personality=st.selectbox("Select a personality",personalities.keys(),placeholder="Choose one.... ",)
    
    st.header("Upload file")
    uploaded_file = st.file_uploader("Upload a file")
    
    if uploaded_file:
        st.success("File uploaded successfully!")
        with st.expander("Preview"):
            context=uploaded_file.read().decode("utf-8")
            st.write(context)

    st.header("Clear Chat")
    if st.button("Clear Chat"):
        st.session_state.messages = []  
        st.success("Chat Cleared")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:       
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question=st.chat_input("You: ")
if question:
    with st.chat_message("user"):
        st.write( question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )
    with st.spinner("Coversation in progress..."):
        response = ollama.chat(
        model="llama3.2:3b", 
        messages=[{
            "role":"system",
            "content":personalities[personality]
        }]+st.session_state.messages   
    )
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])

    st.session_state.messages.append(
        {
            "role": "assistant", 
            "content": response["message"]["content"]
        }
    )

