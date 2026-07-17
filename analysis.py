from database import read_data

#calculate Total, Percentage, Grade
def calculate_results():
    df = read_data()
    df["Total"] = df["Math"] + df["Science"] + df["English"]
    df["Percentage"] = round(df["Total"] / 3, 2)

    grades = []

    for per in df["Percentage"]:

        if per >= 90:
            grades.append("A+")

        elif per >= 80:
            grades.append("A")

        elif per >= 70:
            grades.append("B")

        elif per >= 60:
            grades.append("c")
        
        elif per >= 50:
            grades.append("D")
        
        else:
            grades.append("F")
    
    df["Grade"] = grades
    return df

# student ranking

def student_ranking():
    df = calculate_results()
    df = df.sort_values(by="Percentage", ascending = False)
    df["Rank"] = range(1, len(df) + 1)
    print("\n======= STUDENT RANKING ========")
    print(df[["Rank", "Roll No", "Name", "Percentage", "Grade"]])

# subject wise highest marks

def subject_highest():
    df = read_data()

    print("\nHighest Marks")
    print("Math : ", df["Math"].max())
    print("Science : ", df["Science"].max())
    print("English : ", df["English"].max())

# subject wise average 
    
def subject_average():
    df = read_data()

    print("\nAverage Marks")
    print("Math : ", round(df["Math"].mean(),2))
    print("Science : ", round(df["Science"].mean(),2))
    print("English : ", round(df["English"].mean(),2))

# pass fail analysis

def pass_fail():
    df = calculate_results()

    passed = len(df[df["Percentage"] >= 40])
    failed = len(df[df["Percentage"] < 40])

    print("\nPass Student : ",passed)
    print("\nFail Student : ",failed)

#cpga calculation

def calculate_cgpa():
    df = calculate_results()

    df["CGPA"] = round(df["Percentage"] / 9.5, 2)
    print(df[["Roll No", "Name", "Percentage", "CGPA"]])

#complete report

def complete_report():
    df = calculate_results()
    print(df)