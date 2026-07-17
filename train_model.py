import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

df = pd.read_csv("data/students.csv")

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Percentage"] = df["Total"] / 3

X = df[["Math", "Science", "English", "Attendance"]]
y = df["Percentage"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

print("Model Accuracy:", model.score(X_test, y_test))
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")
print("Model Saved Successfully!")
print(model)