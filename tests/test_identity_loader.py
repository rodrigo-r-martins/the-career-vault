import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.identity import IdentityLoader

def run_loader_test():
  loader = IdentityLoader()
  
  print("--- Testing IdentityLoader ---")
  try:
    master = loader.load_master_file()
    print(f"✅ Master file loaded ({len(master)} characters)")
  except Exception as e:
    print(f"❌ Master file failed: {e}")

  snippets = loader.load_snippets()
  if snippets:
    print(f"✅ Found {len(snippets)} snippets")
    for s in snippets:
      print(f"   - {s['filename']}")
  else:
    print("❌ No snippets found in vault/snippets/")

if __name__ == "__main__":
  run_loader_test()