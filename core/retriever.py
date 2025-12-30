from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os
from langchain_core.documents import Document

_DB_LOCATION = os.path.join(os.path.dirname(__file__), "..", "vector_store")
_DB_EXISTS = os.path.exists(_DB_LOCATION)

class SnippetRetriever:
  def __init__(self, collection_name: str = "career_snippets"):
    self.embeddings = OllamaEmbeddings(model="mxbai-embed-large:335m")
    self.vector_store = Chroma(
      collection_name=collection_name,
      persist_directory=_DB_LOCATION,
      embedding_function=self.embeddings,
    )
  
  def add_snippets(self, snippets: list[dict]):
    documents = []
    ids = []
    for s in snippets:
      text = s['content']
      metadata = {"filename": s['filename']}
      document = Document(page_content=text, metadata=metadata, id=s['filename'])
      documents.append(document)
      ids.append(s['filename'])
    self.vector_store.add_documents(documents=documents, ids=ids)

  def get_relevant_snippets(self, query: str, k: int = 3):
    return self.vector_store.similarity_search(query, k=k)

  def get_langchain_retriever(self, k: int = 3):
    return self.vector_store.as_retriever(search_kwargs={"k": k})