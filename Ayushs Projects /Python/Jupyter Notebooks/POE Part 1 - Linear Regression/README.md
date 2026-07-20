# PDAN8411 — POE Part 1: Linear Regression
### Predicting Medical Insurance Charges

---

## Overview

This project builds a Linear Regression model to predict medical insurance charges based on a patient's age, sex, BMI, number of children, smoking status and geographic region. It was completed as Part 1 of the PDAN8411 Programming for Data Analytics 1 Portfolio of Evidence.

The analysis covers the full machine learning pipeline — from data inspection and exploratory data analysis through to model training, evaluation and regularisation.

**Dataset:** [Kaggle — Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)

---

## Project Structure

```
POE Part 1 - Linear Regression/
│
├── POE_Part1_LinearRegression.ipynb   # Main analysis notebook
├── insurance.csv                       # Dataset
└── README.md                           # This file
```

---

## What the Notebook Covers

| Section | Description |
|---|---|
| 1. Import Libraries | All required Python libraries |
| 2. Load Dataset | Load and preview the insurance CSV |
| 3. Data Inspection | Shape, data types, descriptive stats, null check, duplicate check |
| 4. EDA | Univariate, bivariate and multivariate analysis with visualisations |
| 5. Preprocessing | Encoding, VIF check, encoded heatmap, train/test split, scaling |
| 6. Linear Regression | Model training, coefficients table, predictions |
| 7. Evaluation | MAE, MSE, RMSE, R² metrics and actual vs predicted plot |
| 7.5 P-Value Analysis | statsmodels OLS summary and feature significance table |
| 8. Residual Diagnostics | All 4 Linear Regression assumptions checked with plots |
| 9. Regularisation | Ridge, Lasso and Elastic Net with coefficient comparison |
| 10. Model Comparison | All four models compared side by side |

---

## Requirements

Make sure you have Python 3.8 or higher installed. The following libraries are required:

```
pandas
numpy
matplotlib
seaborn
scikit-learn
statsmodels
scipy
jupyter
```

Install all dependencies at once by running:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels scipy jupyter
```

---

## How to Run

### Step 1 — Clone or download the project

If using Git:
```bash
git clone <your-repo-url>
cd "POE Part 1 - Linear Regression"
```

Or simply download and unzip the folder to your machine.

---

### Step 2 — Make sure the dataset is in the same folder

The notebook expects `insurance.csv` to be in the same directory as the notebook file. The folder should look like this:

```
POE Part 1 - Linear Regression/
├── POE_Part1_LinearRegression.ipynb
├── insurance.csv
└── README.md
```

---

### Step 3 — Launch Jupyter Notebook

Open your terminal, navigate to the project folder and run:

```bash
jupyter notebook
```

This will open Jupyter in your browser. Click on `POE_Part1_LinearRegression.ipynb` to open the notebook.

Alternatively, if you are using **JupyterLab**:

```bash
jupyter lab
```

---

### Step 4 — Run the notebook

Once the notebook is open:

- To run all cells from top to bottom: go to **Kernel → Restart & Run All**
- To run one cell at a time: click on a cell and press **Shift + Enter**

> Make sure you run the cells **in order from top to bottom**. Later cells depend on variables created in earlier cells.

---

### Running in VS Code

If you prefer VS Code:

1. Open VS Code and install the **Jupyter extension** (if not already installed)
2. Open the project folder in VS Code
3. Open `POE_Part1_LinearRegression.ipynb`
4. Click **Run All** at the top of the notebook, or run cells individually using the play button

---

## Model Results Summary

| Model | MAE | MSE | RMSE | R² |
|---|---|---|---|---|
| Linear Regression | 0.2607 | 0.1583 | 0.3979 | 0.8295 |
| Ridge | 0.2615 | 0.1586 | 0.3983 | 0.8291 |
| Lasso | 0.2712 | 0.1694 | 0.4116 | 0.8174 |
| Elastic Net | 0.2705 | 0.1664 | 0.4079 | 0.8208 |

The standard Linear Regression model achieved an R² of **0.8295**, meaning the model explains approximately **83% of the variance** in insurance charges.

---

## Key Findings

- **Smoking status** is the single strongest predictor of insurance charges (coefficient = 1.54, correlation = 0.67 with log-transformed charges)
- **Age** is the strongest numerical predictor — charges increase consistently with age
- **BMI** contributes moderate predictive power
- **Sex** and most **region** columns contribute very little — Lasso eliminated two of the three region dummies without a meaningful drop in R²
- A **log transformation** on the target variable was essential to correct right skewness
- All four models performed similarly, confirming no severe overfitting or multicollinearity

---

## Notes

- The dataset originally contained 1 338 records. One duplicate row was identified and removed, leaving **1 337 clean records**
- Categorical features (sex, smoker, region) were One-Hot Encoded using `pd.get_dummies(drop_first=True)`
- StandardScaler was applied to numerical columns only — fitted on training data and applied to test data to prevent data leakage
- All residual diagnostic plots confirm the four assumptions of Linear Regression are satisfied

---

## Author

**Student:** Ayush Harduth
**Module:** PDAN8411 — Programming for Data Analytics 1
**Institution:** The Independent Institute of Education (IIE) — Varsity College
**Year:** 2026
