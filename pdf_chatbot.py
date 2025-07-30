import streamlit as st
from pdf_utils import extract_text_from_pdf, split_text
from semantic_search import build_faiss_index, get_top_k_chunks
from llm_response import get_together_response

def run_pdf_chatbot():
    st.set_page_config(page_title="📚 Smart PDF Chatbot", layout="centered")
    st.title("📚 Chat with your PDF")

    uploaded_file = st.file_uploader("📎 Upload a PDF", type="pdf")

    # Reset session state if new file is uploaded
    if uploaded_file:
        if "last_uploaded_file" not in st.session_state or uploaded_file.name != st.session_state.last_uploaded_file:
            st.session_state.last_uploaded_file = uploaded_file.name
            st.session_state.chunks = None
            st.session_state.index = None
            st.session_state.chunk_list = None
            st.session_state.messages = []

        if st.session_state.chunks is None:
            st.success(f"✅ Uploaded: {uploaded_file.name}")
            raw_text = extract_text_from_pdf(uploaded_file)

            with st.spinner("🔍 Processing PDF..."):
                chunks = split_text(raw_text)
                index, embeddings, chunk_list = build_faiss_index(chunks)
                st.session_state.chunks = chunks
                st.session_state.index = index
                st.session_state.chunk_list = chunk_list

    # Display previous messages
    for msg in st.session_state.get("messages", []):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if uploaded_file and st.session_state.index:
        prompt = st.chat_input("Ask a question about the uploaded PDF...")
        if prompt:
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):
                with st.spinner("🤖 Generating answer..."):
                    context = get_top_k_chunks(prompt, st.session_state.index, st.session_state.chunk_list)
                    answer = get_together_response(context, prompt)
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
