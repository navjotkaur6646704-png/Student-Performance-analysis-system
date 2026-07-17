from database import read_data, save_data
import pandas as pd 

def add_student():
    df = read_data()

    roll = int(input("Enter Roll Number : "))
    name = input("Enter name : ")

    math = int(input("Math Marks: "))
    science = int(input("Science Marks : "))
    english = int(input("English marks : "))

    attendance = float(input("Attendance (%) : "))

    new_student = pd.DataFrame({
        "Roll No" :[roll],
        "Name" :[name],
        "Math" :[math],
        "Science" : [science],
        "English" : [english],
        "Attendance" :[attendance]
    })

    df = pd.concat([df, new_student], ignore_index=True)
    save_data(df)
    print("Student Added Successfully")

def display_students():
    df = read_data()
    print(df)
 
def search_student():
    df = read_data()
    roll = int(input("Enter Roll Number : "))

    student = df[df["Roll No"] == roll]
    if(student.empty):
        print("Student Not Found")
    else:
        print(student)

def update_student():
    df = read_data()
    roll = int(input("Enter Roll Number : "))
    index = df[df["Roll No"]==roll].index

    if len(index) == 0:
        print("Student Not Found")
        return

    i = index[0]

    df.loc[i, "math"] = int(input("New Math Marks : "))
    df.loc[i, "science"] = int(input("New Science Marks : "))
    df.loc[i, "english"] = int(input("New English Marks : "))
    df.loc[i, "attendance"] = float(input("Attendance : "))

    save_data(df)
    print("Updated Successfully")

def delete_student():
    df = read_data()
    roll = int(input("Enter Roll Number : "))
    df = df[df["Roll No"] != roll]

    save_data(df)
    print("Deleted Successfully")