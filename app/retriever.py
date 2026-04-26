from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

db_location = "./chromadb_storage"

def get_retriever(k:int = 5):
    # fetches top-k relevant chunks

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        embedding_function = embeddings,
        persist_directory = db_location,
    )

    return vector_store.as_retriever(search_kwargs={"k":k})

"""
This file loads the vector DB and retrieves relevant chunks
"""