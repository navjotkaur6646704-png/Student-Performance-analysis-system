import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import prediction

st.write("Dashboard Started")

#page configuration 

st.set_page_config(
    page_title = "Student Performance Dashboard",
    page_icon = "🎓",
    layout = "wide"    
)
st.title("🎓 Student Performance Analysis Dashboard")

# Upload CSV file

uploaded_file = st.file_uploader("Upload Student CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("students.csv")

#calculate results

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Percentage"] = round(df["Total"] / 3,2)

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
    
    return "F"

df["Grade"] = df["Percentage"].apply(grade)
df["CGPA"] = round(df["Percentage"] / 9.5, 2)

#KPI cards

col1, col2, col3, col4 = st.columns(4)

col1.metric("students", len(df))
col2.metric("Average %", round(df["Percentage"].mean(), 2))
col3.metric("Highest %", round(df["Percentage"].max(), 2))
col4.metric("Average Attendance", round(df["Attendance"].mean(), 2))

st.divider()

pass_percentage = round(
    (len(df[df["Percentage"] >= 40]) / len(df)) * 100,
    2
)

st.metric("Pass Percentage", f"{pass_percentage}%")

#student table

st.subheader("Search Student")

name = st.text_input("Enter Student Name")

if name:
    resutl = df[df["Name"].str.lower() == name.lower()]

    if len(resutl) > 0:
        st.success("Student Found")
        st.dataframe(resutl)

    else:
        st.error("Student Not Found")

#Ranking

st.subheader("Student Ranking")

rank = df.sort_values(
    by = "Percentage",
    ascending = False
)
rank["Rank"] = range(1, len(rank) +1)

st.dataframe(rank[
    ["Rank", "Roll No", "Name", "Percentage", "Grade"]
])

st.subheader("🏆 Top 5 Students")

top5 = rank.head(5)

st.dataframe(top5)

# percentage chart

st.subheader("Student Percentage")
fig, ax = plt.subplots(figsize=(12, 5))

ax.bar(df["Name"], df["Math"])

plt.xticks(rotation=45, ha="right", fontsize=9)
plt.tight_layout()

st.pyplot(fig)
# grade distribution

st.subheader("Grade Distribution")
grade_count = df["Grade"].value_counts()
fig2, ax2 = plt.subplots()

ax2.pie(
    grade_count,
    labels = grade_count.index,
    autopct = "%1.1f%%" 
)
st.pyplot(fig2)


st.subheader("Filter by Grade")

grade = st.selectbox(
    "Select Grade",
    ["All", "A+", "A", "B", "C", "D", "F"]
)

if grade != "All":
    st.dataframe(df[df["Grade"] == grade])
else:
    st.dataframe(df)

#subject average

st.subheader("Subject Average")
subjects = ["Math", "Science", "English"]

avg = [
    df["Math"].mean(),
    df["Science"].mean(),
    df["English"].mean()
]

fig3, ax3 = plt.subplots()
ax3.bar(subjects, avg)
st.pyplot(fig3)

#attendance

st.subheader("Attendance")

st.dataframe(
    df[
        ["Roll No", "Name", "Attendance"]
    ]
)

#dowmload report

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download CSV Report",
    csv,
    "Student_Report.csv"
    "text/csv"
)
