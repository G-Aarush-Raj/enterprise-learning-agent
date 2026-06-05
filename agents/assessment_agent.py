def assess_readiness(score):

    if score >= 80:
        return {
            "status": "Ready",
            "recommendation": "Schedule certification exam."
        }

    elif score >= 70:
        return {
            "status": "Almost Ready",
            "recommendation": "Practice weak areas."
        }

    else:
        return {
            "status": "Needs Improvement",
            "recommendation": "Continue studying and take more practice tests."
        }