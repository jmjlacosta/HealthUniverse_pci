import streamlit as st
from PIL import Image

# Load and display the image
image = Image.open("m_kwaa244f1.jpeg")

# Title
st.title("Pediatric Comorbidity Index Calculator")

# Input for age
age = st.number_input("Enter Age (in years):", min_value=0, max_value=18, step=1)

# Define mental and clinical conditions
mental_disorders = {
    "Anxiety or panic disorder": 1,
    "Depression": 4,
    "Drug abuse or dependence": 3,
    "Eating disorders": 1,
    "Psychotic disorders": 3,
    "Conduct disorders": 1,
    "Sleep disorders": 1,
    "Alcohol abuse or dependence": 1,
    "Smoking": 2,
}

clinical_conditions = {
    "Anemia": 2,
    "Any malignancy": 5,
    "Asthma": 1,
    "Cardiovascular conditions": 2,
    "Chromosomal anomalies": 2,
    "Congenital malformations": 2,
    "Developmental delays": 1,
    "Diabetes mellitus": 4,
    "Epilepsy or convulsions": 4,
    "Gastrointestinal conditions": 1,
    "Pain conditions": 1,
    "Weight loss": 2,
    "Joint disorders": 1,
    "Menstrual disorders": 2,
    "Nausea and vomiting": 1,
}

# Columns for mental and clinical conditions
col1, col2 = st.columns(2)

# Checkboxes for mental disorders
with col1:
    st.subheader("Psychiatric and Behavioral Conditions")
    selected_conditions = [score for condition, score in mental_disorders.items() if st.checkbox(condition)]

# Checkboxes for clinical conditions
with col2:
    st.subheader("Somatic and Systemic Conditions")
    selected_conditions += [score for condition, score in clinical_conditions.items() if st.checkbox(condition)]

# Calculate index
if st.button("Calculate Index"):
    index_score = sum(selected_conditions)
    
    # Display score and image
    st.write(f"Pediatric Comorbidity Index Score: {index_score}")
    st.image(image, caption="Observed and Predicted Hospitalization Proportion by Index Score", width=300)

    # Risk level classification
    if index_score == 0:
        risk_category = "<1% Risk of Hospitalization"
    elif index_score in [1, 2, 3]:
        risk_category = "~2% Risk of Hospitalization"
    elif index_score in [4, 5, 6]:
        risk_category = "~5% Risk of Hospitalization"
    elif index_score in [7, 8, 9]:
        risk_category = "~10% Risk of Hospitalization"
    else:
        risk_category = "~30% Risk of Hospitalization"
    
    st.write(f"Risk Category: {risk_category}")

    # Adjust C-statistic based on age group
    if age < 2:
        c_stat = 0.667
        ci_lower, ci_upper = 0.649, 0.684
    elif 2 <= age <= 5:
        c_stat = 0.690
        ci_lower, ci_upper = 0.677, 0.704
    elif 6 <= age <= 11:
        c_stat = 0.705
        ci_lower, ci_upper = 0.694, 0.715
    else:
        c_stat = 0.718
        ci_lower, ci_upper = 0.712, 0.723
    
    st.write(f"C-statistic: {c_stat} (95% CI: {ci_lower} - {ci_upper})")
