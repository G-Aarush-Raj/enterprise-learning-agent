def generate_study_plan(certification, recommended_hours):
    weeks = 4

    hours_per_week = round(recommended_hours / weeks, 1)

    plan = {
        "certification": certification,
        "duration_weeks": weeks,
        "hours_per_week": hours_per_week,
        "milestones": [
            "Learn fundamentals",
            "Practice labs",
            "Take mock assessments",
            "Final revision"
        ]
    }

    return plan