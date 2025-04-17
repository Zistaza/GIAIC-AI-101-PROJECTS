import streamlit as st  # ✅ Streamlit import FIRST
st.set_page_config(page_title="BMI Calculator", layout="centered")  # ✅ MUST BE FIRST streamlit command

import pandas as pd
import matplotlib.pyplot as plt

# Define helper functions (these can come after set_page_config)
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 🟡"
    elif 18.5 <= bmi < 25:
        return "Normal 🟢"
    elif 25 <= bmi < 30:
        return "Overweight 🟠"
    else:
        return "Obese 🔴"

def health_advice(category):
    advice = {
        "Underweight 🟡": "Consider increasing your calorie intake to gain weight.",
        "Normal 🟢": "Keep up the good work! Maintain a balanced diet and regular exercise.",
        "Overweight 🟠": "Consider a more active lifestyle and balanced diet to lose weight.",
        "Obese 🔴": "It's advisable to consult with a healthcare provider to work on a healthy weight loss plan."
    }
    return f"<p style='color:magenta; font-weight:bold;'>{advice.get(category, '')}</p>"

def plot_bmi(bmi):
    categories = ['Underweight', 'Normal', 'Overweight', 'Obese']
    ranges = [18.5, 25, 30, 50]
    colors = ['#FFDD00', '#00FF00', '#FF6600', '#FF0000']

    fig, ax = plt.subplots()
    ax.barh(categories, ranges, color=colors)
    ax.axvline(bmi, color='blue', linestyle='--', label=f'Your BMI: {bmi}')
    ax.set_xlabel('BMI')
    ax.set_title('BMI Categories')
    ax.legend()
    st.pyplot(fig)

def main():
    st.title("💪 BMI Calculator")
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.5)
    height = st.number_input("Enter your height (cm):", min_value=30.0, step=0.5)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        st.success(f"Your BMI is **{bmi}**")
        st.info(f"Category: **{category}**")
        st.markdown(health_advice(category), unsafe_allow_html=True)
        plot_bmi(bmi)

if __name__ == "__main__":
    main()
