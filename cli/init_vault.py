import click
from core.identity import IdentityLoader
from core.retriever import MasterRetriever, SnippetRetriever

def init_vault():
    """Initialize the vault and index all your data."""
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

