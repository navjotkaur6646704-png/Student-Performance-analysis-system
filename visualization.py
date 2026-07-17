import matplotlib.pyplot as plt
from analysis import calculate_results

# create distribution chart

def grade_distribution():
    df = calculate_results()
    grade_count = df["Grade"].value_counts()

    plt.figure(figsize=(6,6))
    plt.pie(
        grade_count,
        labels = grade_count.index,
        autopct = "%1.1f%%",
        startangle = 90
    )

    plt.title("Grade Distribution")
    plt.show()

# student percentage chart

def percentage_chart():
    df = calculate_results()

    plt.figure(figsize=(8,5))
    plt.bar(df["Name"], df["Percentage"])

    plt.title("Student Percentage")
    plt.xlabel("Students")
    plt.ylabel("Percentage")

    plt.show()

#subject average chart

def subject_average_chart():
    df = calculate_results()
    subjects = ["Math", "Science", "English"]

    average = [
        df["Math"].mean(),
        df["Science"].mean(),
        df["English"].mean(),
    ]

    plt.figure(figsize=(6,5))
    plt.bar(subjects, average)

    plt.title("Subject Wise Average")
    plt.ylabel("Average Marks")
    plt.show()