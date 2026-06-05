from agents.learning_agent import get_learning_path
from agents.planner_agent import generate_study_plan
from agents.engagement_agent import get_study_recommendation
from agents.assessment_agent import assess_readiness

learning = get_learning_path("Cloud Engineer")

plan = generate_study_plan(
    learning["certification"],
    learning["recommended_hours"]
)

print(plan)
print(get_study_recommendation("EMP-001"))

print(assess_readiness(67))
print(assess_readiness(82))