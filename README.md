# Medical Insurance Prediction

## Project Overview
This project predicts **medical insurance charges** using a **Machine Learning model**. It uses users' personal and health-related information such as **age, sex, BMI, smoking status, and number of children** to estimate insurance costs.

**Live Demo:** [Medical Insurance Prediction App](https://medical-insurance-prediction-aypo.onrender.com)

---

## Features
- Predict individual medical insurance charges
- Input features:
  - **Age** – Patient's age
  - **Sex** – Male/Female
  - **BMI** – Body Mass Index
  - **Children** – Number of dependents
  - **Smoker** – Yes/No
  - **Region** – Residential region
- Provides accurate predictions using a trained ML model

---

## Installation
1. Clone the repository:
  git clone <repo-url>
  cd <repository-folder>

2. Create and activate a virtual environment:
  python -m venv myenv
  myenv\Scripts\activate       # Windows

3. Install required packages:
  pip install -r requirements.txt


### Usage

1. Run the application locally:
   python app.py

2. Provide input values through the interface

3. See predicted insurance charges as output

### Dataset
Dataset is available in CSV format
Features include: age, sex, bmi, children, smoker, region, charges

### Model

Model: Linear Regression / Random Forest

Evaluated using Train/Test split

Metrics: RMSE, R² score


