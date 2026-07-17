from database import read_data

#attendance report

def attendance_report():
    df = read_data()
    print("\nAttendance Report\n")
    print(df[["Roll No", "Name", "Attendance"]])

#attendance analysis

def attendance_analysis():
    df = read_data()
    average = round(df["Attendance"].mean(),2)
    highest = df["Attendance"].max()
    lowest = df["Attendance"].min()

    print("\nAverage Attendance : ", average,"%")
    print("Highest Attendance : ", highest,"%")
    print("Lowest Attendance : ", lowest,"%")
    