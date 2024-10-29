# Pediatric Comorbidity Index (PCI) App

This repository contains an implementation of the Pediatric Comorbidity Index (PCI), developed to estimate hospitalization risk for pediatric patients based on their comorbid conditions. The PCI score is calculated by summing weighted contributions of specific conditions, with weights derived from logistic regression coefficients, and adjusted to improve comorbidity prediction accuracy.

This tool supports healthcare providers in assessing hospitalization risk, aiding clinical decisions for pediatric patients with multiple health issues.

## How It Works

The PCI model calculates a score based on patient-specific comorbidities. These comorbidities are assigned weights that reflect their impact on hospitalization risk, and the final PCI score categorizes patients into defined risk levels.

### **Input:**
Users select relevant conditions for a pediatric patient, such as anemia, developmental delays, asthma, epilepsy, etc., from a checklist.

### **Output:**
The app returns a PCI score and hospitalization risk level based on observed data:
- **<1% Risk:** Score of 0
- **~2% Risk:** Scores of 1–3
- **~5% Risk:** Scores of 4–6
- **~10% Risk:** Scores of 7–9
- **~30% Risk:** Score ≥10

A visualization compares the patient's risk against observed hospitalization rates.

## Model Details

The PCI model was developed using ICD-10-CM data, evaluated through logistic regression. Two candidate models were considered: one with predefined predictors, and another with both predefined and empirically identified predictors. Elastic net regularization minimized overfitting, selecting key predictors. Ten-fold cross-validation determined the optimal tuning parameter (λ), which controls shrinkage. 

Weights were derived by dividing model coefficients by 0.30 and rounding to the nearest integer, based on methods shown to improve predictive accuracy in comorbidity indices. Each patient’s PCI score is calculated by summing the weights for relevant conditions.

## Summary

The PCI App is a user-friendly tool for healthcare professionals to assess pediatric hospitalization risk. It identifies high-risk patients early, enabling more targeted interventions and personalized care.
