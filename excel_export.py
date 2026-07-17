from analysis import calculate_results

def export_excel():
    df = calculate_results()

    df.to_excel("Student_Report.xlsx", index=False)
    print("\nReport Exported Successfully")
    print("File Name : Student_Report.xlsx" )