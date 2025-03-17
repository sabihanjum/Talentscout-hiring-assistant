# prompts.py

def greeting_prompt():
    return "Hello! I'm TalentScout, your AI Hiring Assistant. I'm here to help with your job application process. Let's get started by gathering some details."

def info_prompt():
    return "Please share your: \n1. Full Name\n2. Email Address\n3. Phone Number\n4. Years of Experience\n5. Desired Position(s)\n6. Current Location\n7. Tech Stack (languages, frameworks, databases, tools)"

def generate_tech_questions_prompt(tech_stack):
    return (
        f"Generate 3-5 technical interview questions for the following tech stack: {tech_stack}. "
        "Questions should test core understanding and practical application of each technology mentioned."
    )

def fallback_prompt():
    return "I'm sorry, I didn't quite understand that. Could you please rephrase?"
