import streamlit as st
import pandas as pd
import PyPDF2
import matplotlib.pyplot as plt

# Page Title
st.title("🚀 AI Resume Analyzer")

# Load Skills Dataset
skills = pd.read_csv("skills_dataset.csv")


# Extract Text From PDF
def extract_text(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text


# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file is not None:

    resume_text = extract_text(uploaded_file)

    found_skills = []

    for skill in skills['skills']:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    missing = list(set(skills['skills']) - set(found_skills))

    score = int((len(found_skills) / len(skills['skills'])) * 100)

    st.subheader("📊 Resume Score")
    st.write(score)

    if score > 70:
        st.success("Excellent Resume")
    elif score > 40:
        st.warning("Good but needs improvement")
    else:
        st.error("Needs Improvement - Add more skills")

    st.subheader("❌ Missing Skills")
    st.write(missing)

    st.subheader("📈 Skill Analysis Chart")

    labels = ["Skills Found", "Missing Skills"]
    values = [len(found_skills), len(missing)]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')

    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')

    st.pyplot(fig)
