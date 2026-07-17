import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------Show banner at the top------------
st.image("banner.png", use_container_width=True)

# Title
st.title("🎓 Student Performance Analysis Dashboard")
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ---------------- UPLOAD CSV ----------------
uploaded_file = st.file_uploader(
    "Upload Student CSV File",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("students.csv")

# ---------------- CALCULATIONS ----------------
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Percentage"] = round(df["Total"] / 3, 2)


def grade(per):
    if per >= 90:
        return "A+"
    
    elif per >= 80:
        return "A"
    
    elif per >= 70:
        return "B"
    
    elif per >= 60:
        return "C"
    
    elif per >= 50:
        return "D"
    else:
        return "F"


df["Grade"] = df["Percentage"].apply(grade)
df["CGPA"] = round(df["Percentage"] / 9.5, 2)

# ---------------- KPI ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Students", len(df))
col2.metric("Average %", round(df["Percentage"].mean(), 2))
col3.metric("Highest %", round(df["Percentage"].max(), 2))
col4.metric("Average Attendance", round(df["Attendance"].mean(), 2))

st.divider()

pass_percentage = round(
    (len(df[df["Percentage"] >= 40]) / len(df)) * 100,
    2
)

st.metric("Pass Percentage", f"{pass_percentage}%")

# ---------------- SEARCH ----------------
st.subheader("🔍 Search Student")

name = st.text_input("Enter Student Name")

if name:
    result = df[df["Name"].str.lower() == name.lower()]

    if len(result) > 0:
        st.success("Student Found")
        st.dataframe(result)
    else:
        st.error("Student Not Found")

# ---------------- RANKING ----------------
st.subheader("🏅 Student Ranking")

rank = df.sort_values(
    by="Percentage",
    ascending=False
)

rank["Rank"] = range(1, len(rank) + 1)

st.dataframe(
    rank[
        ["Rank", "Roll No", "Name", "Percentage", "Grade"]
    ]
)

# ---------------- TOP 5 ----------------
st.subheader("🏆 Top 5 Students")

top5 = rank.head(5)

st.dataframe(top5)

# ---------------- BAR CHART ----------------
st.subheader("📊 Student Percentage")

fig, ax = plt.subplots(figsize=(12, 5))

ax.bar(df["Name"], df["Percentage"])

plt.xticks(rotation=45)

st.pyplot(fig)

# ---------------- PIE CHART ----------------
st.subheader("🎯 Grade Distribution")

grade_count = df["Grade"].value_counts()

fig2, ax2 = plt.subplots()

ax2.pie(
    grade_count,
    labels=grade_count.index,
    autopct="%1.1f%%"
)

st.pyplot(fig2)

# ---------------- FILTER ----------------
st.subheader("🎓 Filter by Grade")

selected_grade = st.selectbox(
    "Select Grade",
    ["All", "A+", "A", "B", "C", "D", "F"]
)

if selected_grade == "All":
    st.dataframe(df)
else:
    st.dataframe(df[df["Grade"] == selected_grade])

# ---------------- SUBJECT AVERAGE ----------------
st.subheader("📚 Subject Average")

subjects = ["Math", "Science", "English"]

avg = [
    df["Math"].mean(),
    df["Science"].mean(),
    df["English"].mean()
]

fig3, ax3 = plt.subplots()

ax3.bar(subjects, avg)

st.pyplot(fig3)

# ---------------- ATTENDANCE ----------------
st.subheader("📅 Attendance")

st.dataframe(
    df[
        ["Roll No", "Name", "Attendance"]
    ]
)

# ---------------- DOWNLOAD ----------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="Student_Report.csv",
    mime="text/csv"
)
