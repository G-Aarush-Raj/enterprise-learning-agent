from services.grok_client import client, MODEL

def generate_manager_recommendation(ready, risk):

    prompt = f"""
    Team Metrics

    Ready Learners: {ready}
    At Risk Learners: {risk}

    Analyze:
    1. Team readiness
    2. Key risks
    3. Recommended actions
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a workforce learning analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content