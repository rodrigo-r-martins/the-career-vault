import click
from core.identity import IdentityLoader
from core.retriever import MasterRetriever, SnippetRetriever
import os
import sys

@click.group()
def cli():
  """The Career Vault: AI-powered job applications."""
  pass

@cli.command()
def init():
  click.echo("🚀 Initializing your Career Vault...")
  loader = IdentityLoader()
  master_content = loader.load_master_file()
  snippets = loader.load_snippets()
  click.echo("📝 Indexing Master Resume...")
  master_retriever = MasterRetriever()
  master_retriever.add_master(master_content)
  click.echo(f"🧩 Indexing {len(snippets)} snippets...")
  snippet_retriever = SnippetRetriever()
  snippet_retriever.add_snippets(snippets)
  click.echo("✨ Vault is ready for action!")

@cli.command()
@click.option("--company", prompt="Company Name", help="The name of the company you are applying to.")
@click.option("--role", prompt="Job Role", help="The title of the position.")
def apply(company, role):
  click.echo(f"🛠️ Preparing application for {role} at {company}...")

  app_folder = f"applications/{company}_{role}".replace(" ", "_")
  os.makedirs(app_folder, exist_ok=True)
  
  click.echo("📋 Paste the Job Description below.")
  click.echo("(Once finished, press Enter then Ctrl+D to save on Mac/Linux)")
  click.echo("-----------------------------------------------------------")
  jd_content = sys.stdin.read().strip()

  if not jd_content:
    click.echo("❌ No Job Description provided. Aborting.")
    return

  jd_path = os.path.join(app_folder, "jd.txt")
  with open(jd_path, "w", encoding="utf-8") as f:
    f.write(jd_content)

  click.echo(f"✅ Application folder created at: {app_folder}")
  click.echo("🔍 Analyzing JD and searching for relevant snippets...")

  retriever = SnippetRetriever()
  relevant_docs = retriever.get_relevant_snippets(jd_content, k=3)
  
  click.echo("\n--- Top Matching Snippets Found ---")
  for doc in relevant_docs:
    click.echo(f"- {doc.metadata.get('filename', 'Unknown')}")

if __name__ == "__main__":
  cli()