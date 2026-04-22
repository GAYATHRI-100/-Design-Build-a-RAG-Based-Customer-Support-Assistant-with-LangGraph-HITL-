from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
import config

def create_vector_store(chunks):
    embeddings = OllamaEmbeddings(model=config.MODEL_NAME)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=config.DB_DIR
    )

    db.persist()
    return db