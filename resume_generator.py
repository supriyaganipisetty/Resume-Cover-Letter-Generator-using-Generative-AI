import cohere
import os

def generate_resume_and_cover(user_data):
    print("Calling Cohere API with:", user_data)

    # You can set this in your environment or paste it directly for testing (not recommended for production)
    cohere_api_key = os.getenv("KxOxP1jPb0l3qwjBp81YlT8zfbjkBu3jTub1A8Wp")
    client = cohere.Client(cohere_api_key)

    prompt = f"""
    Create a resume and a professional cover letter for the following user:
    Name: {user_data['name']}
    Education: {user_data['education']}
    Experience: {user_data['experience']}
    Job Role: {user_data['job_role']}
    Return resume and cover letter separately. Start cover letter with 'Cover Letter:'.
    """

    response = client.generate(
        model='command-r-plus',  # or 'command-r' if you're on free-tier
        prompt=prompt,
        max_tokens=800,
        temperature=0.7
    )

    content = response.generations[0].text
    parts = content.split("Cover Letter:")
    resume = parts[0].strip()
    cover = parts[1].strip() if len(parts) > 1 else "No cover letter found."
    return resume, cover
