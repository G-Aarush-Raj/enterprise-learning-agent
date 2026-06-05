from services.grok_client import client, MODEL

def generate_learning_path(role, certification, skills):

    prompt = f"""
    You are a Learning Path Curator Agent.

    Role: {role}
    Certification: {certification}

    Skills:
    {skills}

    Create:

    1. Learning sequence
    2. Key focus areas
    3. Common mistakes
    4. Suggested timeline
    """

    response = client.chat.completions.create(
        model=MODEL,
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