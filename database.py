import pandas as pd 
import os

DATA_FOLDER = "data"
FILE_NAME = os.path.join(DATA_FOLDER, "students.csv")

columns = [
    "Roll No",
    "Name",
    "Math",
    "Science",
    "English",
    "Attendance"
]

def create_database():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns = columns)
        df.to_csv(FILE_NAME, index=False)

def read_data():
    create_database()
    return pd.read_csv(FILE_NAME)

def save_data(df):
    df.to_csv(FILE_NAME, index=False)