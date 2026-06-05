import json

def get_team_insights():

    with open("data/learners.json", "r") as f:
        learners = json.load(f)

    total = len(learners)

    ready = sum(
        1 for learner in learners
        if learner["practice_score"] >= 80
    )

    risk = total - ready

    if risk > ready:
        recommendation = (
            "Team requires additional preparation before certification exams."
        )
    else:
        recommendation = (
            "Team is progressing well and appears exam-ready."
        )

    return {
        "total_learners": total,
        "ready_for_exam": ready,
        "at_risk": risk,
        "recommendation": recommendation
    }