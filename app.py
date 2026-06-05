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
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Enterprise Learning Multi-Agent System")
st.markdown(
    "AI-powered certification planning, engagement, assessment, and workforce readiness platform."
)

# -----------------------------
# User Inputs
# -----------------------------

role = st.selectbox(
    "Select Employee Role",
    ["Cloud Engineer", "DevOps Engineer"]
)

score = st.slider(
    "Practice Score",
    0,
    100,
    70
)

# -----------------------------
# Generate Workflow
# -----------------------------

if st.button("Generate Learning Journey"):

    # Load Certification Data
    with open("data/certifications.json", "r") as f:
        certifications = json.load(f)

    cert_data = next(
        item for item in certifications
        if item["role"] == role
    )

    certification = cert_data["id"]
    skills = ", ".join(cert_data["skills"])

    # Load Workload Data
    with open("data/workload.json", "r") as f:
        workload_data = json.load(f)

    employee = workload_data[0]

    # -----------------------------
    # Learning Agent
    # -----------------------------

    with st.spinner("🧠 Learning Agent Creating Learning Path..."):

        learning_path = generate_learning_path(
            role=role,
            certification=certification,
            skills=skills
        )

    # -----------------------------
    # Planner Agent
    # -----------------------------

    with st.spinner("📅 Planner Agent Building Study Plan..."):

        study_plan = generate_ai_study_plan(
            role=role,
            certification=certification
        )

    # -----------------------------
    # Engagement Agent
    # -----------------------------

    with st.spinner("🚀 Engagement Agent Personalizing Learning..."):

        engagement_plan = generate_engagement_plan(
            employee["meeting_hours"],
            employee["focus_hours"],
            employee["preferred_slot"]
        )

    # -----------------------------
    # Assessment Agent
    # -----------------------------

    with st.spinner("📝 Assessment Agent Generating Questions..."):

        assessment = generate_assessment(
            certification
        )

    # -----------------------------
    # Manager Insights
    # -----------------------------

    insights = get_team_insights()

    with st.spinner("👨‍💼 Manager Agent Analyzing Team Readiness..."):

        manager_report = generate_manager_recommendation(
            insights["ready_for_exam"],
            insights["at_risk"]
        )

    # -----------------------------
    # Dashboard Metrics
    # -----------------------------

    st.divider()

    st.header("📊 Team Readiness Dashboard")

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

    # -----------------------------
    # Readiness Chart
    # -----------------------------

    labels = ["Ready", "At Risk"]
    values = [
        insights["ready_for_exam"],
        insights["at_risk"]
    ]

    fig, ax = plt.subplots()

    ax.bar(labels, values)

    ax.set_title("Team Readiness Overview")

    st.pyplot(fig)

    # -----------------------------
    # Learner Readiness
    # -----------------------------

    st.header("🎯 Learner Readiness")

    if score >= 80:
        st.success("Ready for Certification Exam")

    elif score >= 70:
        st.warning("Almost Ready - More Practice Recommended")

    else:
        st.error("Needs Additional Preparation")

    # -----------------------------
    # Agent Outputs
    # -----------------------------

    st.divider()

    with st.expander("🧠 Learning Path Agent", expanded=True):
        st.write(learning_path)

    with st.expander("📅 Study Planner Agent"):
        st.write(study_plan)

    with st.expander("🚀 Engagement Agent"):
        st.write(engagement_plan)

    with st.expander("📝 Assessment Agent"):
        st.write(assessment)

    with st.expander("👨‍💼 Manager Insights Agent"):
        st.write(manager_report)

    # -----------------------------
    # Summary
    # -----------------------------

    st.divider()

    report = f"""
    ENTERPRISE LEARNING REPORT

    Role: {role}
    Certification: {certification}

    ==============================
    LEARNING PATH
    ==============================

    {learning_path}

    ==============================
    STUDY PLAN
    ==============================

    {study_plan}

    ==============================
    ENGAGEMENT PLAN
    ==============================

    {engagement_plan}

    ==============================
    ASSESSMENT
    ==============================

    {assessment}

    ==============================
    MANAGER INSIGHTS
    ==============================

    {manager_report}
    """

    st.download_button(
        label="📥 Download Full Report",
        data=report,
        file_name="enterprise_learning_report.txt",
        mime="text/plain"
    )

    st.header("✅ Multi-Agent Workflow Complete")

    st.success(
        "Learning Path → Study Planner → Engagement → Assessment → Manager Insights completed successfully."
    )