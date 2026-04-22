from modules.loader import load_pdf
from modules.chunker import chunk_docs
from modules.embeddings import create_vector_store
from modules.retriever import get_retriever
from modules.graph import build_graph

def setup_system():
    print("📄 Loading PDF...")
    docs = load_pdf("data/support.pdf")

    print("✂️ Chunking...")
    chunks = chunk_docs(docs)

    print("🔢 Creating vector DB...")
    db = create_vector_store(chunks)

    retriever = get_retriever(db)

    print("🔀 Building workflow...")
    graph = build_graph()

    return graph, retriever

def run():
    graph, retriever = setup_system()

    print("\n✅ RAG Support Assistant Ready!")
    print("Type 'exit' to quit\n")

    while True:
        query = input("🧑 Ask: ")

        if query.lower() == "exit":
            break

        result = graph.invoke({
            "query": query,
            "retriever": retriever
        })

        print("\n💬 Answer:", result["answer"], "\n")

if __name__ == "__main__":
    run()