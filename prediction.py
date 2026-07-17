import streamlit as st
import joblib

model = joblib.load("models/model.pkl")

math = float(input("Math: "))
science = float(input("Science: "))
english = float(input("English: "))
attendance = float(input("Attendance: "))

prediction = model.predict([[math, science, english, attendance]])

print("\nPredicted Percentage:", round(prediction[0], 2))

#streamlit prediction

st.header("🎯 Predict Student Performance")

math = st.number_input("Math", 0, 100)
science = st.number_input("Science", 0, 100)
english = st.number_input("English", 0, 100)
attendance = st.number_input("Attendance", 0, 100)

import joblib

model = joblib.load("models/model.pkl")

if st.button("Predict"):

    prediction = model.predict([[math, science, english, attendance]])

    st.success(
        f"Predicted Percentage: {prediction[0]:.2f}%"
    )

# Predict Grade
if prediction >= 90:
    grade = "A+"
elif prediction >= 80:
    grade = "A"
elif prediction >= 70:
    grade = "B"
elif prediction >= 60:
    grade = "C"
elif prediction >= 50:
    grade = "D"
else:
    grade = "F"

st.success(f"Predicted Grade: {grade}")