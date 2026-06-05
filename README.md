# Enterprise Learning Multi-Agent System

## Overview

Enterprise Learning Multi-Agent System is an AI-powered platform designed to help organizations manage employee certification and learning programs efficiently. The system uses multiple specialized AI agents that collaborate to generate personalized learning paths, adaptive study plans, engagement strategies, readiness assessments, and manager-level workforce insights.

The project demonstrates multi-agent reasoning, agent orchestration, enterprise learning workflows, and AI-powered decision-making using synthetic organizational data.

---

## Features

### 🧠 Learning Path Agent

* Analyzes employee roles and certification goals.
* Generates personalized learning roadmaps.
* Identifies key focus areas and common mistakes.

### 📅 Study Planner Agent

* Creates detailed certification study schedules.
* Recommends weekly milestones and study checkpoints.
* Adapts plans based on certification requirements.

### 🚀 Engagement Agent

* Generates personalized learning engagement strategies.
* Recommends optimal study timings.
* Provides motivation and burnout prevention guidance.

### 📝 Assessment Agent

* Generates certification readiness questions.
* Provides answers and learning validation.
* Supports continuous learning evaluation.

### 👨‍💼 Manager Insights Agent

* Analyzes team readiness metrics.
* Identifies workforce learning risks.
* Recommends actions for improving certification success rates.

---

## Multi-Agent Architecture

```text
User
 │
 ▼
Learning Path Agent
 │
 ▼
Study Planner Agent
 │
 ▼
Engagement Agent
 │
 ▼
Assessment Agent
 │
 ▼
Manager Insights Agent
 │
 ▼
Final Learning Report
```

The system follows a sequential multi-agent workflow where each agent contributes specialized intelligence to generate a comprehensive enterprise learning experience.

---

## Technology Stack

* Python
* Streamlit
* Grok AI (xAI API)
* JSON Synthetic Datasets
* Matplotlib
* Git & GitHub

---

## Synthetic Data

This project uses only synthetic data and does not contain any real employee information or personally identifiable information (PII).

### Dataset Categories

* Employee Profiles
* Certification Requirements
* Learning Progress Metrics
* Team Readiness Metrics
* Workload Signals

Example:

```json
{
  "learner_id": "L-1001",
  "role": "Cloud Engineer",
  "certification": "AZ-204",
  "practice_score": 67
}
```

---

## Dashboard Components

### Team Readiness Dashboard

Displays:

* Total Learners
* Ready for Certification
* At-Risk Learners

### Learning Journey Generation

Generates:

* Learning Path
* Study Plan
* Engagement Strategy
* Assessment Questions
* Manager Insights

### Readiness Analytics

Visualizes team readiness using charts and metrics.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/enterprise-learning-agent.git
cd enterprise-learning-agent
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
XAI_API_KEY=your_grok_api_key
```

### Run Application

```bash
streamlit run app.py
```

---

## Screenshots

### Dashboard

Add screenshot:

```text
screenshots/dashboard.png
```

### Agent Outputs

Add screenshot:

```text
screenshots/agent_outputs.png
```

### Team Readiness Analytics

Add screenshot:

```text
screenshots/readiness_chart.png
```

---

## Future Enhancements

* Microsoft Foundry Integration
* Azure AI Deployment
* Role-Based Access Control
* Real-Time Analytics Dashboard
* PDF Report Generation
* Team Progress Tracking
* Certification Recommendation Engine
* Learning Performance Forecasting

---

## Responsible AI

This project follows responsible AI principles:

* Uses synthetic data only.
* Does not process personal information.
* Provides recommendations for educational purposes.
* Maintains transparency in AI-generated outputs.

---

## Author

Aarush Raj Gandhari

Enterprise Learning Multi-Agent System demonstrates how multiple AI agents can collaborate to create intelligent, explainable, and scalable enterprise learning experiences.
