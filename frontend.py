from rag_pipeline import answer_query, retrieve_docs, llm_model
import streamlit as st

uploaded_file = st.file_uploader("Upload PDF", type='pdf', accept_multiple_files=True)

# Chatbot Skeleton
user_query = st.text_area("Enter your Prompt: ", height= 150, placeholder="Ask Anything!")

ask_question = st.button("Ask AI")

if ask_question:

    if uploaded_file:

        st.chat_message("User").write(user_query)

        # RAG Pipeline Call
        retrieved_docs = retrieve_docs(user_query)  # FAISS DB will do a Similarity Search & give relevent Documents
        response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
        st.chat_message("AI Lawyer").write(response.content)

    else:
        st.error("Please Enter a Valid PDF File!!")




