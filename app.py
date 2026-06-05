import streamlit as st
import matplotlib.pyplot as plt
from agents.learning_agent import get_learning_path
from agents.planner_agent import generate_study_plan
from agents.engagement_agent import get_study_recommendation
from agents.assessment_agent import assess_readiness
from agents.manager_agent import get_team_insights

st.title("Enterprise Learning Multi-Agent System")

role = st.selectbox(
    "Select Role",
    ["Cloud Engineer", "DevOps Engineer"]
)

if st.button("Generate Learning Plan"):

    learning = get_learning_path(role)

    plan = generate_study_plan(
        learning["certification"],
        learning["recommended_hours"]
    )

    engagement = get_study_recommendation("EMP-001")
    score = st.slider(
        "Practice Score",
        0,
        100,
        70
    )

    readiness = assess_readiness(score)

    insights = get_team_insights()

    labels = ["Ready", "At Risk"]
    values = [
        insights["ready_for_exam"],
        insights["at_risk"]
    ]
    fig, ax = plt.subplots()
    ax.bar(labels, values)

    st.pyplot(fig)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Learners", insights["total_learners"])

    with col2:
        st.metric("Ready for Exam", insights["ready_for_exam"])

    with col3:
        st.metric("At Risk", insights["at_risk"])

    st.subheader("Learning Path")
    st.json(learning)

    st.subheader("Study Plan")
    st.json(plan)

    st.subheader("Engagement Recommendation")
    st.success(engagement)

    st.subheader("Readiness Assessment")
    st.json(readiness)

    st.subheader("Manager Insights")
    st.json(insights)