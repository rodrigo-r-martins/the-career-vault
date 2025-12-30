from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os
from langchain_core.documents import Document

_DB_LOCATION = os.path.join(os.path.dirname(__file__), "..", "vector_store")
_DB_EXISTS = os.path.exists(_DB_LOCATION)

_MASTER_COLLECTION_NAME = "career_master"
_SNIPPET_COLLECTION_NAME = "career_snippets"

class BaseRetriever:
  def __init__(self, collection_name: str):
    self.embeddings = OllamaEmbeddings(model="mxbai-embed-large:335m")
    self.vector_store = Chroma(
      collection_name=collection_name,
      persist_directory=_DB_LOCATION,
      embedding_function=self.embeddings,
    )
  
  def add_documents(self, documents: list[Document], ids: list[str] = None):
    self.vector_store.add_documents(documents=documents, ids=ids)
  
  def get_relevant_documents(self, query: str, k: int = 3):
    return self.vector_store.similarity_search(query, k=k)
  
  def get_langchain_retriever(self, k: int = 3):
    return self.vector_store.as_retriever(search_kwargs={"k": k})

class MasterRetriever(BaseRetriever):
  def __init__(self):
    super().__init__(collection_name=_MASTER_COLLECTION_NAME)
  
  def add_master(self, master: str):
    document = Document(page_content=master, metadata={"filename": "master.md"})
    self.add_documents(documents=[document])

  def get_relevant_master(self, query: str, k: int = 3):
    return self.get_relevant_documents(query=query, k=k)

  def get_langchain_retriever(self, k: int = 3):
    return self.get_langchain_retriever(k=k)

class SnippetRetriever(BaseRetriever):
  def __init__(self):
    super().__init__(collection_name=_SNIPPET_COLLECTION_NAME)
  
  def add_snippets(self, snippets: list[dict]):
    documents = [Document(page_content=s['content'], metadata={"filename": s['filename']}, id=s['filename']) for s in snippets]
    ids = [s['filename'] for s in snippets]
    self.add_documents(documents=documents, ids=ids)

  def get_relevant_snippets(self, query: str, k: int = 3):
    return self.get_relevant_documents(query=query, k=k)

  def get_langchain_retriever(self, k: int = 3):
    return self.get_langchain_retriever(k=k)