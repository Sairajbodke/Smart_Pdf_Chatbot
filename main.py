import streamlit as st
from pdf_chatbot import run_pdf_chatbot

# 🏠 Homepage
def run_homepage():
    st.set_page_config(page_title="Welcome | Smart PDF Chatbot", layout="centered")
    st.title("🤖 Smart PDF Chatbot Assistant")

    # Centered image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("chatbot.jpg", width=200)  # Ensure chatbot.jpg is in the same folder

    st.markdown("""
    ### 📄 What You Can Do Here:
    - Upload any PDF document
    - Ask detailed questions from it
    - Get smart, human-like answers
    - Powered by Together AI and Semantic Search (FAISS + Transformers)

    ---
    > 🚀 Click the **Start Chatbot** option from sidebar to begin chatting with your PDF!
    """)

# Sidebar navigation
page = st.sidebar.selectbox("📂 Choose a Page", ["Home", "PDF Chatbot"])

if page == "Home":
    run_homepage()
elif page == "PDF Chatbot":
    run_pdf_chatbot()
