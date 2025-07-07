
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
import os

def get_rag_chain():
    # Get full path to vector store
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    vector_path = os.path.join(base_path, "faiss_medical")

    # Load vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(vector_path, embeddings, allow_dangerous_deserialization=True)

    # Setup retriever and LLM
    retriever = db.as_retriever(search_kwargs={"k": 3})
    llm = Ollama(model="llama3")  # Ensure you’ve pulled this model via `ollama run llama3`

    # Build the RAG chain
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    return chain
