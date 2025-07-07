from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import os

def build_vector_db():
    texts = []
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    for file in os.listdir(base_path):
        if file.endswith(".txt"):
            with open(os.path.join(base_path, file), 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    texts.append(content)

    if not texts:
        print("❌ No text files found or all files are empty!")
        return

    print(f"✅ Found {len(texts)} article(s)")

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = text_splitter.create_documents(texts)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.from_documents(docs, embeddings)
    vector_db.save_local(os.path.join(base_path, "faiss_medical"))

if __name__ == "__main__":
    build_vector_db()
