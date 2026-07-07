import streamlit as st
import google.generativeai as genai

# Secrets se key utha raha hai
genai.configure(api_key=st.secrets["AQ.Ab8RN6I8xt5YfI600qRGz5PylSdrDx6ALZpHxza0eJIJkjZwHg"])

st.title("Mera AI Chatbot")

# Chat history ko maintain karne ke liye
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chats display karne ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User ka input
if prompt := st.chat_input("Mujhse kuch bhi poocho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini se jawab lena
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
