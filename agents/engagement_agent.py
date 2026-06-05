from services.grok_client import client, MODEL

def generate_engagement_plan(
    meeting_hours,
    focus_hours,
    preferred_slot
):

    prompt = f"""
    Employee Profile

    Meeting Hours: {meeting_hours}
    Focus Hours: {focus_hours}
    Preferred Slot: {preferred_slot}

    Create:

    1. Reminder strategy
    2. Best study timing
    3. Burnout prevention advice
    4. Motivation message
    """

    response = client.chat.completions.create(
        model=MODEL,
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