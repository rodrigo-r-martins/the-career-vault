import click
from cli import (
    init_vault,
    apply_to_job,
    tailor_resume,
    generate_cover_letter,
    answer_job_questions
)

@click.group()
def cli():
    """The Career Vault: Your AI-powered job application assistant."""
    pass

@cli.command()
def init():
    """Initialize the vault and index all your data."""
    init_vault()

@cli.command()
@click.option("--company", prompt="Company Name", help="The name of the company.")
@click.option("--role", prompt="Job Role", help="The title of the position.")
def apply(company, role):
    """Start a new job application tailoring process."""
    apply_to_job(company, role)

@cli.command(name="tailor_resume")
@click.argument("folder")
def tailor_resume_cmd(folder):
    """Update your resume based on the JD in the specified folder."""
    tailor_resume(folder)

@cli.command()
@click.argument("folder")
def cover_letter(folder):
    """Generate a cover letter for the specified application folder."""
    generate_cover_letter(folder)

@cli.command()
@click.argument("folder")
def answer_questions(folder):
    """Answer job-specific questions for the specified application folder."""
    answer_job_questions(folder)

if __name__ == "__main__":
    cli()
