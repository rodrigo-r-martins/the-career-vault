import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.identity import IdentityLoader
from core.retriever import SnippetRetriever

def run_retriever_test():
  print("--- Testing SnippetRetriever ---")
  loader = IdentityLoader()
  snippets = loader.load_snippets()
  
  retriever = SnippetRetriever()
  
  print("Indexing snippets...")
  retriever.add_snippets(snippets)
  
  query = "Experience with Shopify and AI bots"
  print(f"Searching for: '{query}'")
  
  results = retriever.get_relevant_documents(query=query, k=2)
  
  if results:
    for i, doc in enumerate(results):
      source = doc.metadata.get('filename', 'Unknown')
      print(f"✅ Match #{i+1} found in: {source}")
  else:
    print("❌ No matches returned from Vector Store.")

if __name__ == "__main__":
  run_retriever_test()