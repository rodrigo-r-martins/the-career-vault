from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

class CareerAgent:
  def __init__(self):
    self.model = OllamaLLM(model="deepseek-r1:8b")

  def update_resume(self, resume: str, job_description: str) -> str:
    template = """
    You are an expert Technical Recruiter. Your job is to update my resume to match the job description.
    Adjust the wording, responsibilities, and achievements so they fit what the role is looking for.
    Keep the tone professional and consistent with the rest of my resume.
    
    Here is my resume:
    {resume}
    Here is the job description:
    {job_description}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | self.model
      
    return chain.invoke({"resume": resume, "job_description": job_description})
  
  def generate_cover_letter(self, job_description: str, relevant_snippets: str) -> str:
    template = """
    You are an expert Technical Recruiter. Your job is to generate a cover letter for me to apply to the job.
    Write your cover letter in a natural, conversational style and use human-like language. Use the job description to help you generate the cover letter.
    Don't use bullet points - just full, flowing sentences.

    Here are some relevant snippets from my resume:
    {relevant_snippets}

    Here is the job description:
    {job_description}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | self.model
    return chain.invoke({"job_description": job_description, "relevant_snippets": relevant_snippets})
  
  def answer_questions(self, questions: list[str], job_description: str, experience_context: str) -> str:
    template = """
    You are an expert Technical Recruiter. 
    Your job is to answer the provided questions using the candidate's EXPERIENCE CONTEXT.
    Write your answers in a natural, conversational style. Keep your answers short and 
    concise (1 paragraph, max 4-5 sentences) and use human-like language. Use the job 
    description to help you answer the questions.
    Don't use bullet points - just full, flowing sentences.
    
    CANDIDATE EXPERIENCE:
    {experience_context}

    JOB DESCRIPTION:
    {job_description}

    QUESTIONS TO ANSWER:
    {questions}

    Write your answers in a natural, conversational style. Keep each answer concise.
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | self.model
    return chain.invoke({
        "questions": questions, 
        "job_description": job_description,
        "experience_context": experience_context
    })