from services.grok_client import client, MODEL

def generate_ai_study_plan(role, certification):

    prompt = f"""
    Create a detailed 4-week study plan.

    Role: {role}
    Certification: {certification}

    Include:
    - Weekly goals
    - Study hours
    - Practice checkpoints
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are an enterprise study planner."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content