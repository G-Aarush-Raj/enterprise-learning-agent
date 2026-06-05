from services.grok_client import client, MODEL

def generate_ai_study_plan(role, certification):

    prompt = f"""
    Create a detailed 4-week certification study plan.

    Role: {role}
    Certification: {certification}

    Include:
    - Weekly milestones
    - Daily study recommendations
    - Practice checkpoints
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are an enterprise learning planner."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content