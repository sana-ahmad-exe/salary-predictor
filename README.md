# Salary Predictor
This project predicts salary from years of experience using one Linear
Regression model. The Streamlit app loads a saved model and displays a
prediction when the user changes the experience value.
## Dataset
Source:
https://github.com/SagarChhabriya/data-science/blob/main/datasets/TBD/salary_dataset.csv
The dataset has 200 rows and two numeric columns: Experience Years and
Salary. There are no missing values or duplicate rows, so no filling or
row removal was needed. Salary currency and time period are unspecified.
## Model and evaluation
Model: Linear Regression from scikit-learn.
Feature: Experience Years.
Target: Salary.
Split: 80 percent training and 20 percent testing, random_state=42.
Test MAE: 4056.3438613897365
Test R squared: 0.9831368268457784
The notebook explores the data, trains and evaluates the model, and saves
it as model.pkl. The app loads that file without retraining. Predictions
are estimates from this dataset, not guaranteed salaries.
## Run locally on Windows
Clone this repository and open its folder in VS Code.
Create and activate the environment in PowerShell:
    py -3.13 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
Select the .venv kernel in model.ipynb, run all cells in order, and save.
Then start the app from the project folder:
    python -m streamlit run app.py
Open the Local URL shown in the terminal.
## Files- salary_dataset.csv: dataset.- model.ipynb: data exploration, training, evaluation and serialization.- model.pkl: saved trained model.- app.py: Streamlit interface.- requirements.txt: library versions.- .gitignore: excludes the local virtual environment.
## Live application
https://salary-predictor-4ufukmddblabykyqpbsevd.streamlit.app/