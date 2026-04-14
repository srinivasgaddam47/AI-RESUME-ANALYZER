import streamlit as st
import pandas as pd
import PyPDF2

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
st.title("🚀 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    resume_text = extract_text(uploaded_file)

    found_skills = match_skills(resume_text)

    score = len(found_skills) / len(skills) * 100

    st.subheader("📊 Resume Score")
    st.progress(int(score))
    st.write(f"{score:.2f}%")

    st.subheader("✅ Skills Found")
    st.write(found_skills)

    missing = list(set(skills['skills']) - set(found_skills))

    st.subheader("❌ Missing Skills")
    st.write(missing)

    role = predict_role(found_skills)

    st.subheader("🎯 Recommended Role")
    st.success(role)

    st.subheader("📈 Suggestions")

    if score > 70:
        st.success("Excellent Resume")
    elif score > 40:
        st.warning("Good but needs improvement")
    else:
        st.error("Needs Improvement - Add more skills")
import matplotlib.pyplot as plt
missing = list(set(skills['skills']) - set(found_skills))

st.subheader("❌ Missing Skills")
st.write(missing)


# Skill Chart (Paste Here)
st.subheader("📊 Skill Analysis Chart")

labels = ["Skills Found", "Missing Skills"]
values = [len(found_skills), len(missing)]

fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%')
st.pyplot(fig)

if score > 80:
    st.success(" Excellent Resume")
elif score > 60:
    st.info("Good Resume")
elif score > 40:
    st.warning("⚠ Moderate Resume")
else:
    st.error("❌ Weak Resume — Improve Skills")
report = f"""
Resume Score: {score:.2f}%

Skills Found:
{found_skills}

Missing Skills:
{missing}

Recommended Role:
{role}
"""

st.download_button(
    label="📄 Download Report",
    data=report,
    file_name="resume_report.txt",
    mime="text/plain"
)
st.subheader("📌 Resume Level")

if score >= 80:
    st.success("Advanced Level Resume")
elif score >= 50:
    st.info("Intermediate Level Resume")
else:
    st.warning("Beginner Level Resume")
st.subheader("🎯 Recommended Skills to Learn")

recommended = missing[:5]
st.write(recommended)
st.title("🚀 AI Resume Analyzer & Career Advisor")
st.caption("Hackathon Project — AI Powered Resume Evaluation System")