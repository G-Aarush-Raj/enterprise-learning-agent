from services.openai_client import client

def generate_assessment(certification):

    prompt = f"""
    Generate 5 certification readiness questions for {certification}.

    Provide:
    - Question
    - Correct answer
    """

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role": "system",
                "content": "You are a certification assessor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content