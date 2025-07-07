

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from rag.rag_chat import get_rag_chain


st.set_page_config(page_title="🩺 Medical RAG Chatbot")
st.title("🤖 Medical Assistant (RAG + LLaMA)")

# Initialize RAG chain
if "chain" not in st.session_state:
    with st.spinner("Loading model and vector DB..."):
        st.session_state.chain = get_rag_chain()

query = st.text_input("Ask a medical question:")

if query:
    with st.spinner("Thinking..."):
        result = st.session_state.chain(query)
        st.write("### 🧠 Answer:")
        st.success(result['result'])

        with st.expander("📚 Source documents"):
            for doc in result['source_documents']:
                st.markdown(f"**Source:** {doc.metadata.get('source', 'unknown')}")
                st.markdown(doc.page_content[:500] + "...")

# # Mock digital twin display
# st.image("https://i.imgur.com/Yj4BQJm.png", caption="Digital Twin Mock", use_column_width=True)
