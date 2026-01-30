from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

_DB_LOCATION = os.path.join(os.path.dirname(__file__), "..", "vector_store")
_DB_EXISTS = os.path.exists(_DB_LOCATION)

_MASTER_COLLECTION_NAME = "career_master"
_SNIPPET_COLLECTION_NAME = "career_snippets"

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, # Max characters per chunk
    chunk_overlap=100 # Keep a little bit of the previous chunk for context
)

class BaseRetriever:
  def __init__(self, collection_name: str):
    self.embeddings = OllamaEmbeddings(model=os.getenv("MODEL_EMBEDDING"))
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
    """Splits the master resume into chunks and indexes them."""
    # 1. Break the large text into smaller chunks
    chunks = text_splitter.split_text(master)
    
    # 2. Turn those chunks into Documents
    documents = []
    ids = []
    for i, chunk in enumerate(chunks):
      doc = Document(page_content=chunk, metadata={"filename": "master.md", "chunk": i}, id=f"master_chunk_{i}")
      documents.append(doc)
      ids.append(f"master_chunk_{i}") # Unique ID for each chunk
    self.add_documents(documents=documents, ids=ids)

  def get_relevant_master(self, query: str, k: int = 3):
    return self.get_relevant_documents(query=query, k=k)

class SnippetRetriever(BaseRetriever):
  def __init__(self):
    super().__init__(collection_name=_SNIPPET_COLLECTION_NAME)
  
  def add_snippets(self, snippets: list[dict]):
    all_documents = []
    all_ids = []
    
    for s in snippets:
      chunks = text_splitter.split_text(s['content'])
      for i, chunk in enumerate(chunks):
        doc = Document(
          page_content=chunk, 
          metadata={"filename": s['filename'], "chunk": i},
          id=f"{s['filename']}_chunk_{i}"
        )
        all_documents.append(doc)
        all_ids.append(f"{s['filename']}_chunk_{i}")
    self.add_documents(documents=all_documents, ids=all_ids)

  def get_relevant_snippets(self, query: str, k: int = 3):
    return self.get_relevant_documents(query=query, k=k)

  def get_langchain_retriever(self, k: int = 3):
    return super().get_langchain_retriever(k=k)