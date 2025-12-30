import os

class IdentityLoader:
  def __init__(self, vault_path: str = "vault") -> None:
    self.vault_path = vault_path
    self.master_file_path = os.path.join(self.vault_path, "master.md")
    self.snippets_path = os.path.join(self.vault_path, "snippets")
    
  def load_master_file(self) -> str:
    if not os.path.exists(self.master_file_path):
      raise FileNotFoundError(f"Master file not found at {self.master_file_path}")
    with open(self.master_file_path, "r", encoding="utf-8") as file:
      return file.read()
  
  def load_snippets(self) -> list[str]:
    snippets = []
    if not os.path.exists(self.snippets_path):
      return snippets
    for filename in os.listdir(self.snippets_path):
      if filename.endswith(".md"):
        file_path = os.path.join(self.snippets_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
          snippets.append({
            "filename": filename,
            "content": file.read()
          })
    return snippets
