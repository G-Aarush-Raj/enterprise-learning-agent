from agents.learning_agent import get_learning_path
from agents.planner_agent import generate_study_plan
from agents.engagement_agent import get_study_recommendation
from agents.assessment_agent import assess_readiness
from agents.manager_agent import get_team_insights

print("\n=== Enterprise Learning Agent ===\n")

role = input("Enter Role: ")

learning = get_learning_path(role)

if learning:

    plan = generate_study_plan(
        learning["certification"],
        learning["recommended_hours"]
    )

    engagement = get_study_recommendation("EMP-001")

    readiness = assess_readiness(67)

    insights = get_team_insights()

    print("\n--- Learning Path ---")
    print(learning)

    print("\n--- Study Plan ---")
    print(plan)

    print("\n--- Engagement Recommendation ---")
    print(engagement)

    print("\n--- Readiness Assessment ---")
    print(readiness)

    print("\n--- Manager Insights ---")
    print(insights)

else:
    print("Role not found.")