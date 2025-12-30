import sys
import os
# Path helper to allow importing from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agent import CareerAgent

def test_agent_features():
    agent = CareerAgent()
    
    # Sample data for testing
    sample_jd = "We need a Python developer with experience in Shopify APIs and AI bots."
    sample_resume = "I am a developer with 5 years of Python experience. I built a movie database."
    sample_snippets = "Project: Shopify Integration. Details: Built a custom checkout flow for a major retailer."
    sample_questions = ["How have you used AI in your projects?", "Tell us about your Shopify experience."]

    print("\n" + "="*50)
    print("🚀 STARTING AGENT TESTS")
    print("="*50)

    print("\n--- 1. Testing Resume Tailoring ---")
    print("(DeepSeek is thinking...)")
    resume_result = agent.update_resume(sample_resume, sample_jd)
    # Removing potential <think> tags for cleaner output display
    clean_resume = resume_result.split("</think>")[-1].strip()
    print("✅ Result (Preview):", clean_resume[:200], "...\n")

    print("--- 2. Testing Cover Letter Generation ---")
    print("(DeepSeek is thinking...)")
    cl_result = agent.generate_cover_letter(sample_jd, sample_snippets)
    clean_cl = cl_result.split("</think>")[-1].strip()
    print("✅ Result (Preview):", clean_cl[:200], "...\n")

    print("--- 3. Testing Application Q&A ---")
    print("(DeepSeek is thinking...)")
    qa_result = agent.answer_questions(sample_questions, sample_jd, sample_snippets)
    clean_qa = qa_result.split("</think>")[-1].strip()
    print("✅ Result (Preview):", clean_qa[:200], "...")
    
    print("\n" + "="*50)
    print("✨ ALL AGENT TESTS COMPLETED")
    print("="*50)

if __name__ == "__main__":
    test_agent_features()

