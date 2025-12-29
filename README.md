# The Career Vault 🛡️💼

An AI-powered career assistant that manages your professional identity and automates job application tailoring. This project uses a local-first approach with a file-system based state for transparency and auditability.

## 🚀 Overview

The Career Vault stores your "Master Resume" and project-specific deep dives (snippets) as Markdown files. When you apply for a job, it analyzes the job description, selects the most relevant parts of your experience, and generates tailored resumes and cover letters.

## ✨ Key Features

- **Identity Loader:** Smart context filtering of your professional history.
- **Multi-Agent Workflow:** Orchestrated steps using a Reflective Loop (Analyst, Matcher, Writer, Reviewer).
- **CLI-Driven:** A professional terminal experience for managing your career data.
- **Local & Private:** Runs locally using **Ollama** (defaulting to `deepseek-r1:8b`) to keep your data private.
- **Mock Interviews:** (Coming Soon) AI-driven mock interviews based on your tailored applications.

## 🛠️ Tech Stack

- **AI Framework:** LangChain & LangGraph
- **LLM:** Ollama (Local)
- **CLI Framework:** Click
- **Vector Store:** ChromaDB (for snippet retrieval)
- **Environment:** Python 3.13+

## ⚙️ Setup & Installation

1. **Install Ollama:** Follow instructions at [ollama.com](https://ollama.com).
2. **Pull the Model:**
   ```bash
   ollama pull deepseek-r1:8b
   ```
3. **Setup Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## 📂 Project Structure

```text
career_vault/
├── main.py             # CLI entry point
├── core/
│   ├── identity.py     # Data loading & filtering
│   ├── agent.py        # LLM Orchestration
│   └── storage.py      # File system operations
├── vault/              # YOUR DATA (Master resume & snippets)
└── applications/       # Tailored outputs
```

## 🛠️ Usage (Development)

Currently in initial development. Run the test script:

```bash
python main.py
```
