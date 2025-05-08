import streamlit as st                                                   #used for web UI
from langchain.chains import ConversationalRetrievalChain                #used for enabling Q&A chain
from langchain.memory import ConversationBufferMemory                    #tracks history and remembers past message

from pdf_utils import extract_text_from_pdf
from vector_store import create_retriever
from llm_setup import load_llm

# basic page design
st.set_page_config(page_title="PDF Chatbot (Local LLM)", layout="wide")
st.title("🤖 Chat with your PDF using TinyLlama (Offline)")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])          #allows user to upload pdf
query = st.text_input("Ask a question about the PDF")                   #takes text input from user

if uploaded_file and query:
    with st.spinner("Processing..."):
        text = extract_text_from_pdf(uploaded_file)                     #writen in pdf utils

        if not text.strip():
            st.error("❌ No extractable text found.")
            st.stop()

        retriever = create_retriever(text)                              #writen in vector store to split doc in chunks....
        llm = load_llm()

        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )

        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            memory=memory,
            return_source_documents=True,
            output_key="answer"
        )

        response = qa_chain.invoke({"question": query})
        st.success(response["answer"])
