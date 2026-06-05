from services.grok_client import client, MODEL

def generate_assessment(certification):

    prompt = f"""
    Generate 5 certification readiness questions.

    Certification: {certification}

    For each question provide:
    - Question
    - Correct Answer
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a certification assessment expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content