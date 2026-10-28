
import streamlit as st
import pandas as pd

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
h1 {
    color: #17365d;
}
h2, h3 {
    color: #24527a;
}
[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #e0e6ef;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🎓 Student Performance Analysis Chatbot")
st.write(
    "An intelligent study assistant to analyze academic "
    "performance and support student improvement."
)

st.divider()

# ---------------- SIDEBAR / TEAM ----------------
st.sidebar.title("👥 Our Project Team")
st.sidebar.write("**Member 1:** Your Name")
st.sidebar.write("**Member 2:** Teammate Name")
st.sidebar.write("**Member 3:** Teammate Name")
st.sidebar.write("**Member 4:** Teammate Name")

st.sidebar.divider()
st.sidebar.info(
    "Project: Student Performance Analysis Chatbot"
)

st.sidebar.write("**Technology**")
st.sidebar.write("Python")
st.sidebar.write("Streamlit")
st.sidebar.write("Pandas")

# ---------------- STUDENT DETAILS ----------------
st.header("📝 Student Information")

name = st.text_input("Student Name")

st.subheader("📚 Enter Subject Marks")

col1, col2, col3 = st.columns(3)

with col1:
    maths = st.number_input(
        "Mathematics (out of 100)",
        min_value=0,
        max_value=100,
        value=0
    )

with col2:
    science = st.number_input(
        "Science (out of 100)",
        min_value=0,
        max_value=100,
        value=0
    )

with col3:
    english = st.number_input(
        "English (out of 100)",
        min_value=0,
        max_value=100,
        value=0
    )

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0,
    max_value=100,
    value=75
)

analyze = st.button(
    "🔍 Analyze My Performance",
    type="primary",
    use_container_width=True
)

# ---------------- PERFORMANCE ANALYSIS ----------------
if analyze:

    total = maths + science + english
    percentage = total / 3

    subjects = {
        "Mathematics": maths,
        "Science": science,
        "English": english
    }

    strongest = max(subjects, key=subjects.get)
    weakest = min(subjects, key=subjects.get)

    st.divider()
    st.header("📊 Performance Dashboard")

    st.write(
        f"Welcome, **{name.strip() if name.strip() else 'Student'}**!"
    )

    # Metrics
    c1, c2, c3 = st.columns(3)

    c1.metric("Total Marks", f"{total}/300")
    c2.metric("Average Score", f"{percentage:.1f}%")
    c3.metric("Attendance", f"{attendance}%")

    # Performance feedback
    st.subheader("💡 Performance Summary")

    if percentage >= 80:
        st.success(
            "Excellent performance! Keep up your hard work."
        )
    elif percentage >= 60:
        st.info(
            "Good performance! Regular practice can help you improve."
        )
    elif percentage >= 40:
        st.warning(
            "You need more practice in some areas. "
            "Focus on understanding difficult concepts."
        )
    else:
        st.error(
            "Your marks suggest that you may benefit from "
            "additional revision and a structured study plan."
        )

    # Subject chart
    st.subheader("📈 Subject-Wise Performance")

    chart_data = pd.DataFrame({
        "Subject": list(subjects.keys()),
        "Marks": list(subjects.values())
    })

    st.bar_chart(
        chart_data,
        x="Subject",
        y="Marks",
        y_label="Marks out of 100"
    )

    # Strengths and improvement
    st.subheader("🎯 Strengths and Areas to Improve")

    c1, c2 = st.columns(2)

    with c1:
        st.success(f"Strongest subject: {strongest}")

    with c2:
        st.warning(f"Subject to focus on: {weakest}")

    st.write(
        f"Suggested focus: Spend extra revision time on **{weakest}**, "
        "practice questions, and review mistakes."
    )

    # Attendance
    st.subheader("📅 Attendance Analysis")

    if attendance >= 75:
        st.success("Attendance is at or above the example 75% threshold.")
    else:
        st.warning(
            "Attendance is below the example 75% threshold. "
            "Check your institution's attendance requirements."
        )

    # Study recommendations
    st.subheader("📖 Suggested Study Plan")

    for subject, mark in subjects.items():
        if mark < 40:
            st.write(
                f"- **{subject}:** Revise the basics and practise "
                "short questions every day."
            )
        elif mark < 70:
            st.write(
                f"- **{subject}:** Review weak topics and solve "
                "practice questions regularly."
            )
        else:
            st.write(
                f"- **{subject}:** Maintain your progress with "
                "revision and challenging questions."
            )

# ---------------- CHATBOT ----------------
st.divider()
st.header("🤖 Chat With Your Study Assistant")

st.write(
    "Ask questions about studying, marks, attendance, "
    "or improving your academic performance."
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input(
    "Ask: How can I improve my marks?"
)

if question:
    st.session_state.chat_history.append({
        "role": "user",
        "content": question
    })

    q = question.lower()

    if "math" in q:
        answer = (
            "For Mathematics, practise a few problems every day. "
            "Understand the method before memorizing formulas."
        )
    elif "science" in q:
        answer = (
            "For Science, understand concepts, create short notes, "
            "and practise diagrams and questions."
        )
    elif "english" in q:
        answer = (
            "For English, practise reading, grammar, vocabulary, "
            "and short writing exercises regularly."
        )
    elif "attendance" in q:
        answer = (
            "Track your attendance regularly and check the minimum "
            "requirement set by your institution."
        )
    elif "study plan" in q or "timetable" in q:
        answer = (
            "Try this routine: 30 minutes reviewing a weak topic, "
            "30 minutes solving questions, and 15 minutes reviewing "
            "your mistakes. Adjust it to your schedule."
        )
    elif "improve" in q or "low marks" in q:
        answer = (
            "Identify your weakest topics, study them in small sections, "
            "practise questions, and review mistakes every week."
        )
    elif "marks" in q or "performance" in q or "percentage" in q:
        answer = (
            "Enter your subject marks above and click Analyze My "
            "Performance to see your score, chart, and recommendations."
        )
    else:
        answer = (
            "I can help with Mathematics, Science, English, attendance, "
            "study timetables, and improving marks. Ask me about one "
            "of these topics!"
        )

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()

# ---------------- FOOTER ----------------
st.divider()

st.caption(
    "🎓 Student Performance Analysis Chatbot | "
    "Built using Python, Streamlit, and Pandas"
)

st.caption(
    "Educational guidance only. Recommendations are based on "
    "the marks and attendance entered."
)
