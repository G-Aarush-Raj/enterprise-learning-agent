from services.openai_client import client

def generate_learning_path(role, certification, skills):

    prompt = f"""
    You are a Learning Path Curator Agent.

    Role: {role}
    Certification: {certification}

    Skills:
    {skills}

    Create:

    1. Recommended learning sequence
    2. Most important skills to focus on
    3. Common beginner mistakes
    4. Suggested preparation timeline

    Format the response professionally.
    """

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role": "system",
                "content": "You are an enterprise learning specialist."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content