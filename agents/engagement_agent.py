from services.openai_client import client

def generate_engagement_plan(
    meeting_hours,
    focus_hours,
    preferred_slot
):

    prompt = f"""
    You are an Engagement Agent.

    Employee Profile:

    Meeting Hours Per Week: {meeting_hours}
    Focus Hours Per Week: {focus_hours}
    Preferred Learning Slot: {preferred_slot}

    Create:

    1. Personalized study reminder strategy
    2. Best study schedule recommendations
    3. Burnout prevention advice
    4. Weekly motivation message

    Keep the response practical and concise.
    """

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role": "system",
                "content": "You are a workplace learning coach."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content