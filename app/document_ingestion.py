import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

db_location = "./chromadb_storage"

file_path = "./data/SAMSUNG_CARE_Plus_2Years.pdf"

def ingest_pdf(file_path:str):

    # Checks if pdf exists
    if not os.path.exists(file_path):
        raise FileNotFoundError("PDF not found")
    
    #1. load pdf
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    #2. Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 200
    )
    chunks = splitter.split_documents(documents)

    #3. Convert to embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name = "all-MiniLM-L6-v2"
    )

    #4. Store in ChromaDB
    vector_store = Chroma.from_documents(
        documents = chunks,
        embedding = embeddings,
        persist_directory = db_location
    ) 

    print(f"Document Ingestion complete: {len(chunks)} chunks stored")

"""
This file handles:
PDF → Chunking → Embedding → Storage in ChromaDB
"""