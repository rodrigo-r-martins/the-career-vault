import click
import os
import sys
from core.retriever import MasterRetriever, SnippetRetriever
from core.agent import CareerAgent

def answer_job_questions(folder):
    """Answer specific application questions based on your experience."""
    jd_path = os.path.join(folder, "jd.txt")
    if not os.path.exists(jd_path):
        click.echo(f"❌ No jd.txt found in {folder}")
        return

    click.echo("🔍 Fetching your relevant experience...")
    with open(jd_path, "r", encoding="utf-8") as f:
        jd = f.read()
    
    s_retriever = SnippetRetriever()
    m_retriever = MasterRetriever()
    
    snippets = s_retriever.get_relevant_snippets(jd, k=5)
    master_chunks = m_retriever.get_relevant_master(jd, k=3)
    
    experience_context = "\n\n".join([doc.page_content for doc in snippets + master_chunks])

    click.echo("❓ Enter the application questions (one per line, finish with Ctrl+D):")
    questions_text = sys.stdin.read().strip()
    if not questions_text:
        click.echo("❌ No questions provided.")
        return
    
    questions = questions_text.split("\n")
    
    agent = CareerAgent()
    result = agent.answer_questions(questions, jd, experience_context)
    
    output_path = os.path.join(folder, "application_answers.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)
    
    click.echo(f"✅ Answers saved to {output_path}")

