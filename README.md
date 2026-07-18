# Predictive Maintenance: Remaining Useful Life (RUL) Prediction

## Problem Statement

Unplanned equipment downtime is one of the costliest problems in manufacturing operations. This project builds a model to predict the **Remaining Useful Life (RUL)** of turbofan engines using sensor telemetry, simulating the kind of predictive maintenance system used to schedule interventions before failure occurs — directly relevant to preventive maintenance scheduling in a multi-machine production fleet.

## Dataset

[NASA C-MAPSS Turbofan Engine Degradation Simulation Dataset](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/) (public, NASA Prognostics Center of Excellence).

* Multiple engine units run to failure under different operating conditions
* 21 sensor channels + 3 operational settings per timestep
* Goal: predict cycles remaining before failure for each engine unit

## Approach

1. **Exploratory Data Analysis** — sensor degradation trends across engine lifecycle, identify which sensors carry signal vs. noise
2. **Feature Engineering** — rolling statistics (mean/std over sliding windows), RUL labeling (capped at a max threshold per convention in literature)
3. **Modeling** — baseline linear regression → Random Forest / XGBoost regression
4. **Evaluation** — RMSE, MAE, and a visualization of predicted vs. actual RUL curves

## Results

\## Results



| Model | RMSE | MAE |

|---|---|---|

| Linear Regression (baseline) | 46.07 | 35.47 |

| Random Forest (raw sensor features) | 45.84 | 34.34 |

| Random Forest + rolling-window features | 43.70 | 32.27 |



\*\*Key findings:\*\*

\- Of 21 sensor channels, 6 showed meaningful degradation trends (sensors 2, 3, 4, 7, 11, 15) via variance analysis and visual inspection; the remaining sensors were flat and excluded from modeling.

\- Engineering rolling-window (5-cycle) mean features reduced RMSE by \~5% over raw sensor readings, confirming that degradation \*trend\* is more predictive than instantaneous sensor values.

\- Feature importance analysis confirmed this: every rolling-mean feature outranked its raw counterpart in the trained model.

\- Sensor 4 (rolling mean) was the single most important predictor of Remaining Useful Life.



\*\*Interpretation:\*\* Sensors that trend consistently over an engine's lifecycle carry the real predictive signal for failure timing — a finding consistent with how condition-based maintenance programs prioritize monitoring in practice.

!\[Feature Importance](outputs/feature\_importance.png)

&#x20;  !\[Predicted vs Actual RUL](outputs/predicted\_vs\_actual.png)



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

