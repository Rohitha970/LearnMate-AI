import streamlit as st
import json

# Load roadmap data
with open("roadmap_data.json", "r") as file:
    data = json.load(file)

# Page settings
st.set_page_config(page_title="LearnMate AI")

# Title
st.title("🎓 LearnMate AI")
st.subheader("Personalized Course Pathway Agent")

st.write("AI-powered personalized learning assistant for students.")

# User Inputs
name = st.text_input("Enter Your Name")

domain = st.selectbox(
    "Choose Your Interest",
    list(data.keys())
)

level = st.selectbox(
    "Select Skill Level",
    ["Beginner", "Intermediate"]
)

goal = st.text_input("Enter Your Career Goal")

# Generate Button
if st.button("Generate Roadmap"):

    result = data[domain][level]

    st.success(f"Hello {name}! Here is your personalized roadmap.")

    # Skills
    st.write("## 🚀 Skills to Learn")
    for skill in result["skills"]:
        st.write("✅", skill)

    # Courses
    st.write("## 📚 Recommended Courses")
    for course in result["courses"]:
        st.write("📘", course)

    # Projects
    st.write("## 💻 Suggested Projects")
    for project in result["projects"]:
        st.write("🔥", project)

    # Goal
    st.write("## 🎯 Career Goal")
    st.info(goal)

    # AI Guidance
    st.write("## 🤖 AI Guidance")
    st.write(
        f"Based on your interest in {domain}, "
        f"focus on consistent practice and project building."
    )