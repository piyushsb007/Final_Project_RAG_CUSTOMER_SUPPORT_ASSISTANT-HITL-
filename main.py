import os
from app.graph import build_graph
from app.document_ingestion import ingest_pdf

app = build_graph()

DB_PATH = "./chromadb_storage"
PDF_PATH = "data/SAMSUNG_CARE_Plus_2Years.pdf"

def main():
    if not os.path.exists(DB_PATH):
        print("No vector DB found. Running ingestion...")
        ingest_pdf(PDF_PATH)
    else:
        print("Vector DB already exists. Skipping ingestion.")

    history = []

    while True:
        query = input("\nUser: ")

        if query.lower() in ["exit","quit"]:
            print("\nThank you for using the Customer Support Assistant. Have a great day!")
            break

        result = app.invoke({
            "query" : query,
            "context" : "",
            "response": "",
            "category": ""
        })

        print("🤖 Answer: \n",result['response'] )

if __name__ == "__main__":
    main()