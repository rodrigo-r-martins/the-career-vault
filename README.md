# The Career Vault 🛡️💼

An AI-powered career assistant that manages your professional identity and automates job application tailoring. This project uses a local-first approach with a file-system based state for transparency and auditability.

## 🚀 Overview

The Career Vault stores your "Master Resume" and project-specific deep dives (snippets) as Markdown files. When you apply for a job, it analyzes the job description, selects the most relevant parts of your experience, and generates tailored resumes and cover letters.

## ✨ Key Features

- **Identity Loader:** Smart context filtering of your professional history.
- **Multi-Agent Workflow:** Orchestrated steps using a Reflective Loop (Analyst, Matcher, Writer, Reviewer).
- **CLI-Driven:** A professional terminal experience for managing your career data.
- **Local & Private:** Runs locally using **Ollama** to keep your data private.
- **Mock Interviews:** (Coming Soon) AI-driven mock interviews based on your tailored applications.

## 🛠️ Tech Stack

- **AI Framework:** LangChain & LangGraph
- **LLM:** Ollama (Local)
- **CLI Framework:** Click
- **Vector Store:** ChromaDB (for snippet retrieval)
- **Environment:** Python 3.13+

## ⚙️ Setup & Installation

1. **Install Ollama:** Follow instructions at [ollama.com](https://ollama.com).
2. **Pull the Models:**
   ```bash
   # For logic and writing
   ollama pull deepseek-r1:8b
   # For vector indexing
   ollama pull mxbai-embed-large:335m
   ```
3. **Setup Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -e .
   ```

## 🛠️ Usage

After installation, use the `career-agent` command directly from your terminal:

### 1. Initialize the Vault

Index your master resume and snippets into the vector database.

```bash
career-agent init
```

### 2. Start a New Application

Analyze a Job Description and create a dedicated folder for the role.

```bash
career-agent apply
```

### 3. Tailor Your Resume

Update your master resume based on the specific job description.

```bash
career-agent tailor-resume applications/Company_Role
```

### 4. Generate a Cover Letter

Create a human-like cover letter using relevant context from your vault.

```bash
career-agent cover-letter applications/Company_Role
```

### 5. Answer Application Questions

Get tailored answers for specific application questions.

```bash
career-agent answer-questions applications/Company_Role
```
