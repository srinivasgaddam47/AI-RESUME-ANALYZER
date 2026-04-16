import streamlit as st
import pandas as pd
import PyPDF2
import matplotlib.pyplot as plt

# Load Skills Dataset
skills = pd.read_csv("skills_dataset.csv")

# Extract Text from Resume
def extract_text(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

# Match Skills
def match_skills(resume_text):
    found_skills = []
    for skill in skills['skills']:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)
    return found_skills

# Predict Job Role
def predict_role(found_skills):
    if "Python" in found_skills and "SQL" in found_skills:
        return "Data Analyst"
    elif "Machine Learning" in found_skills:
        return "Machine Learning Engineer"
    elif "Excel" in found_skills:
        return "Business Analyst"
    else:
        return "General IT Role"

# UI Design
st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    resume_text = extract_text(uploaded_file)

    found_skills = match_skills(resume_text)

    score = len(found_skills) / len(skills) * 100

    st.subheader("Resume Score")
    st.progress(int(score))
    st.write(f"{score:.2f}%")

    st.subheader("Skills Found")
    st.write(found_skills)

    missing = list(set(skills['skills']) - set(found_skills))

    st.subheader(" Missing Skills")
    st.write(missing)

    role = predict_role(found_skills)

    st.subheader("Recommended Role")
    st.success(role)

    st.subheader(" Suggestions")
if uploaded_file:

    resume_text = extract_text(uploaded_file)

    found_skills = match_skills(resume_text)

    score = len(found_skills) / len(skills) * 100

    st.subheader("Resume Score")
    st.progress(int(score))
    st.write(f"{score:.2f}%")

    st.subheader("Skills Found")
    st.write(found_skills)

    missing = list(set(skills['skills']) - set(found_skills))

    st.subheader("Missing Skills")
    st.write(missing)

    role = predict_role(found_skills)

    st.subheader(" Recommended Role")
    st.success(role)

    st.subheader("Suggestions")

    if score > 70:
        st.success("Excellent Resume")
    elif score > 40:
        st.warning("Good but needs improvement")
    else:
        st.error("Needs Improvement - Add more skills")

    # Skill Chart
    st.subheader("Skill Analysis Chart")

    labels = ["Skills Found", "Missing Skills"]
    values = [len(found_skills), len(missing)]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')

    st.pyplot(fig)
