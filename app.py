import streamlit as st
import matplotlib.pyplot as plt
import json

from agents.learning_agent import generate_learning_path
from agents.planner_agent import generate_ai_study_plan
from agents.engagement_agent import generate_engagement_plan
from agents.assessment_agent import generate_assessment
from agents.manager_agent import (
    get_team_insights,
    generate_manager_recommendation
)

st.set_page_config(
    page_title="Enterprise Learning Multi-Agent System",
    layout="wide"
)

st.title("🎓 Enterprise Learning Multi-Agent System")

role = st.selectbox(
    "Select Role",
    ["Cloud Engineer", "DevOps Engineer"]
)

score = st.slider(
    "Practice Score",
    0,
    100,
    70
)

if st.button("Generate AI Learning Plan"):

    with open("data/certifications.json", "r") as f:
        certifications = json.load(f)

    cert_data = next(
        item for item in certifications
        if item["role"] == role
    )

    certification = cert_data["id"]
    skills = ", ".join(cert_data["skills"])

    with st.spinner("Learning Agent Working..."):
        learning_path = generate_learning_path(
            role,
            certification,
            skills
        )

    with st.spinner("Planner Agent Working..."):
        study_plan = generate_ai_study_plan(
            role,
            certification
        )

    with open("data/workload.json", "r") as f:
        workload = json.load(f)

    employee = workload[0]

    with st.spinner("Engagement Agent Working..."):
        engagement_plan = generate_engagement_plan(
            employee["meeting_hours"],
            employee["focus_hours"],
            employee["preferred_slot"]
        )

    with st.spinner("Assessment Agent Working..."):
        assessment_questions = generate_assessment(
            certification
        )

    insights = get_team_insights()

    with st.spinner("Manager Agent Working..."):
        manager_recommendation = generate_manager_recommendation(
            insights["ready_for_exam"],
            insights["at_risk"]
        )

    st.divider()

    st.subheader("📊 Team Readiness Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Learners",
            insights["total_learners"]
        )

    with col2:
        st.metric(
            "Ready For Exam",
            insights["ready_for_exam"]
        )

    with col3:
        st.metric(
            "At Risk",
            insights["at_risk"]
        )

    labels = ["Ready", "At Risk"]

    values = [
        insights["ready_for_exam"],
        insights["at_risk"]
    ]

    fig, ax = plt.subplots()

    ax.bar(labels, values)

    st.pyplot(fig)

    st.divider()

    st.subheader("🧠 Learning Path Agent")
    st.write(learning_path)

    st.subheader("📅 Study Planner Agent")
    st.write(study_plan)

    st.subheader("🚀 Engagement Agent")
    st.write(engagement_plan)

    st.subheader("📝 Assessment Agent")
    st.write(assessment_questions)

    st.subheader("👨‍💼 Manager Insights Agent")
    st.write(manager_recommendation)

    st.subheader("🎯 Readiness Score")

    if score >= 80:
        st.success("Ready for Certification Exam")
    elif score >= 70:
        st.warning("Almost Ready")
    else:
        st.error("Needs More Preparation")