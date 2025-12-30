import click
import os
import sys
from core.retriever import MasterRetriever, SnippetRetriever

def apply_to_job(company, role):
    """Start a new job application tailoring process."""
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

    click.echo("-----------------------------------------------------------")
    click.echo(f"✅ Job Description saved to {app_folder}/jd.txt")
    
    click.echo("🔍 Analyzing JD and searching for relevant context...")
    s_retriever = SnippetRetriever()
    m_retriever = MasterRetriever()
    
    relevant_snippets = s_retriever.get_relevant_snippets(jd_content, k=3)
    relevant_master = m_retriever.get_relevant_master(jd_content, k=2)
    
    click.echo("\n--- Top Matching Snippets Found ---")
    for doc in relevant_snippets:
        click.echo(f"🧩 Snippet: {doc.metadata.get('filename', 'Unknown')}")
    
    for doc in relevant_master:
        click.echo(f"📄 Master Detail: {doc.page_content[:100]}...")

