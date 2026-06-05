import json

from services.grok_client import client, MODEL


def get_team_insights():

    with open("data/learners.json", "r") as f:
        learners = json.load(f)

    total = len(learners)

    ready = sum(
        1 for learner in learners
        if learner["practice_score"] >= 80
    )

    risk = total - ready

    return {
        "total_learners": total,
        "ready_for_exam": ready,
        "at_risk": risk
    }


def generate_manager_recommendation(
    ready,
    risk
):

    prompt = f"""
    Team Learning Metrics

    Ready Learners: {ready}
    At Risk Learners: {risk}

    Analyze:

    1. Team readiness
    2. Key risks
    3. Recommended actions
    4. Manager summary
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