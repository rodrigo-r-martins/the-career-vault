import click
import os
from core.identity import IdentityLoader
from core.agent import CareerAgent

def tailor_resume(folder):
    """Update your resume based on the JD in the specified folder."""
    jd_path = os.path.join(folder, "jd.txt")
    if not os.path.exists(jd_path):
        click.echo(f"❌ No jd.txt found in {folder}")
        return

    click.echo(f"📝 Tailoring resume for {folder}...")
    
    with open(jd_path, "r", encoding="utf-8") as f:
        jd = f.read()
    
    loader = IdentityLoader()
    master = loader.load_master_file()
    
    agent = CareerAgent()
    result = agent.update_resume(master, jd)
    
    output_path = os.path.join(folder, "tailored_resume.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)
    
    click.echo(f"✅ Tailored resume saved to {output_path}")

