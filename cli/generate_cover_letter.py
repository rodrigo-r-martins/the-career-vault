import click
import os
from core.retriever import MasterRetriever, SnippetRetriever
from core.agent import CareerAgent

def generate_cover_letter(folder):
    """Generate a cover letter based on the JD and relevant snippets."""
    jd_path = os.path.join(folder, "jd.txt")
    if not os.path.exists(jd_path):
        click.echo(f"❌ No jd.txt found in {folder}")
        return

    click.echo(f"✉️ Generating cover letter for {folder}...")
    
    with open(jd_path, "r", encoding="utf-8") as f:
        jd = f.read()
    
    s_retriever = SnippetRetriever()
    m_retriever = MasterRetriever()
    
    snippets = s_retriever.get_relevant_snippets(jd, k=3)
    master_chunks = m_retriever.get_relevant_master(jd, k=2)
    
    context_text = "\n\n".join([doc.page_content for doc in snippets + master_chunks])
    
    agent = CareerAgent()
    result = agent.generate_cover_letter(jd, context_text)
    
    output_path = os.path.join(folder, "cover_letter.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)
    
    click.echo(f"✅ Cover letter saved to {output_path}")

