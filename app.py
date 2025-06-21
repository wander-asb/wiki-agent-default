import streamlit as st
import os
from dotenv import load_dotenv
from services.wiki import search_wikipedia
from chains.qa_chain import qa_chain

st.set_page_config(page_title="Chatbot with Wikipedia", page_icon="🌐")
st.title("🌐 Chatbot with Wikipedia API")

# Interface
question = st.text_input("Ask me anything about a country, concept or person:")


if st.button("Ask"):
    if question:
        with st.spinner("Searching Wikipedia..."):
            context = search_wikipedia(question)

        with st.spinner("Generating answer..."):
            response = qa_chain.invoke({
                "context": context,
                "question": question
            })

        st.subheader("Answer:")
        st.write(response.content)

        st.subheader("Wikipedia Context:")
        st.info(context)
    else:
        st.warning("Please enter a question.")
