from student import *
from analysis import *
from visualization import *
from attendance import *
from excel_export import *

while True:

    print("\n========= STUDENT PERFOMANCE SYSTEM ========")

    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Ranking")
    print("7. Subject Highest Marks")
    print("8. Subject Average")
    print("9. Pass / Fail Analysis")
    print("10. CGPA")
    print("11. Complete Report")
    print("12. Attendance Report")
    print("13. Attendance Analysis")
    print("14.Grade Distribution Chart")
    print("15. Percentage Chart")
    print("16. Subject Average Chart")
    print("17. Export Report to Excel")
    print("18. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        add_student()
    
    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        student_ranking()

    elif choice == 7:
        subject_highest()

    elif choice == 8:
        subject_average()

    elif choice == 9:
        pass_fail()

    elif choice == 10:
        calculate_cgpa()

    elif choice == 11:
        complete_report()

    elif choice == 12:
        attendance_report()

    elif choice == 13:
        attendance_analysis()

    elif choice == 14:
        grade_distribution()

    elif choice == 15:
        percentage_chart()
    
    elif choice == 16:
        subject_average_chart()

    elif choice == 17:
        export_excel()

    elif choice == 18:
        print("Thank You")
        break
    
    else:
        print("Invalid Choice")