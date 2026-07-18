# Predictive Maintenance: Remaining Useful Life (RUL) Prediction

## Problem Statement
Unplanned equipment downtime is one of the costliest problems in manufacturing operations. This project builds a model to predict the **Remaining Useful Life (RUL)** of turbofan engines using sensor telemetry, simulating the kind of predictive maintenance system used to schedule interventions before failure occurs — directly relevant to preventive maintenance scheduling in a multi-machine production fleet.

## Dataset
[NASA C-MAPSS Turbofan Engine Degradation Simulation Dataset](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/) (public, NASA Prognostics Center of Excellence).
- Multiple engine units run to failure under different operating conditions
- 21 sensor channels + 3 operational settings per timestep
- Goal: predict cycles remaining before failure for each engine unit

## Approach
1. **Exploratory Data Analysis** — sensor degradation trends across engine lifecycle, identify which sensors carry signal vs. noise
2. **Feature Engineering** — rolling statistics (mean/std over sliding windows), RUL labeling (capped at a max threshold per convention in literature)
3. **Modeling** — baseline linear regression → Random Forest / XGBoost regression
4. **Evaluation** — RMSE, MAE, and a visualization of predicted vs. actual RUL curves

## Results
*(To be filled in after modeling — target: quantify RMSE improvement from baseline to tuned model, e.g. "Reduced RMSE from X to Y cycles using feature engineering + gradient boosting")*

## Why This Project
This mirrors real-world preventive maintenance scheduling work — predicting when equipment needs servicing before failure, rather than reacting after the fact. It applies a Six Sigma "reduce variation, prevent defects" mindset to a data science workflow.

## Repo Structure
```
predictive-maintenance/
├── data/           # raw and processed data (not committed if large; see data/README)
├── notebooks/       # exploratory analysis and modeling notebooks
├── src/             # reusable Python scripts (data loading, feature engineering, modeling)
├── outputs/          # saved figures, model artifacts, results tables
├── requirements.txt
└── README.md
```

## Tools
Python, pandas, NumPy, scikit-learn, XGBoost, matplotlib/seaborn, Jupyter
