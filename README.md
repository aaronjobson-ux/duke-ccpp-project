<img src="IMG_6655.png" alt="Project Banner" width="100%">
⚡ Combined Cycle Power Plant Forecasting (Duke MLPM)

My analysis and modeling work for the Duke ML Product Management course using the CCPP dataset. This project demonstrates how machine learning can transform raw environmental telemetry into actionable operational intelligence for energy production teams.

---

🌐 Executive Summary

Combined‑cycle power plants experience hourly fluctuations in energy output driven by environmental conditions such as temperature, pressure, humidity, and vacuum. Operators currently respond reactively to these shifts, creating inefficiencies in production planning, fuel allocation, and grid stability.

This project builds a regression‑based forecasting system that converts ambient telemetry into accurate hourly output predictions. The model is designed through an ML Product Management lens — prioritizing interpretability, operational stability, low‑latency inference, and real‑world decision support. The result is a production‑ready forecasting capability that improves plant predictability, reduces waste, and strengthens grid reliability.

---

📘 Project Summary

This project applies a product‑first ML workflow to the Combined Cycle Power Plant (CCPP) dataset. The goal is not only to build accurate regression models, but to demonstrate how ML can solve real operational challenges inside industrial energy systems.

Environmental variables such as temperature, pressure, humidity, and vacuum meaningfully influence turbine efficiency. By modeling these relationships, the system provides proactive insight into expected hourly output — enabling smarter scheduling, resource optimization, and more stable grid operations.

Through structured EDA, baseline modeling, multivariate regression, and operational evaluation, the final model delivers measurable improvements in predictive accuracy while meeting real‑world constraints like low latency, interpretability, and sensor noise resilience.

---

📊 Dataset Summary & Product Engineering Profile

The CCPP dataset includes five continuous variables describing environmental conditions affecting turbine performance. The target variable, net hourly electrical energy output (PE), is predicted using four telemetry inputs:

• Ambient Temperature (AT)
• Exhaust Vacuum (V)
• Ambient Pressure (AP)
• Relative Humidity (RH)


From a deployment perspective, the dataset has a strong engineering profile:

• Low Cost & High Availability — All inputs come from existing plant sensors.
• Near‑Real‑Time Streamability — Continuous physical measurements support low‑latency ingestion.
• Collinearity Risk — Natural environmental interdependence requires careful model selection.
• Simple Validation — Numerical inputs with physical limits simplify production data checks.


---

🔍 EDA Summary

EDA confirms that all four environmental inputs operate within stable physical ranges with zero missing values — a strong indicator of high‑quality industrial telemetry.

Key findings:

• Ambient Temperature (AT) shows the strongest negative correlation with energy output (PE).
• Collinearity exists among temperature, vacuum, and humidity.
• No anomalies or missing values → simple data SLA.


These relationships validate the dataset’s suitability for regression modeling and support establishing an AT‑only baseline before introducing multivariate approaches.

---

🧠 Modeling Approach

The modeling strategy balances interpretability, operational stability, and predictive performance.

1. Baseline Model
A simple AT‑only regression establishes a transparent benchmark and quantifies the incremental value of multivariate modeling.
2. Multivariate Models
Because EDA revealed strong collinearity, the pipeline prioritizes architectures that handle interdependent features:• Regularized linear models (Ridge, Lasso)
• Tree‑based methods

3. Operational Evaluation
Models were assessed for:• Stability across environmental fluctuations
• Resilience to sensor noise
• Low‑latency inference (<50ms)
• Interpretability for operator adoption



The final model — a regularized Ridge regression — delivered meaningful improvements while maintaining production‑ready latency and explainability.

---

📈 Evaluation

Model performance was evaluated using MAE, RMSE, and R², comparing multivariate models against the AT‑only baseline.

Key improvements:

• 15% reduction in RMSE
• 10% lift in R²
• <50ms inferential latency
• Fully interpretable via coefficients + SHAP


Operational stability was prioritized, ensuring consistent performance across environmental fluctuations and real‑time telemetry streams.

---

💡 Product Value

This model drives operational cost savings, grid reliability, and production predictability by converting ambient environmental telemetry into accurate hourly turbine energy‑output forecasts.

It strengthens four high‑impact workflows:

• Smarter Production Planning — Predicts efficiency drops before they occur.
• Resource Optimization — Aligns expected output with fuel, staffing, and maintenance windows.
• Grid & Operational Stability — Provides early visibility into climate‑driven performance swings.
• Low‑Friction Integration — Uses existing sensors and maintains sub‑50ms latency for seamless dashboard deployment.


Ultimately, the model translates ML metrics into tangible improvements in plant predictability, stability, and cost efficiency.

---

🛠️ Tech Stack

Core Tools

• Python 3.10+
• Pandas, NumPy
• Matplotlib, Seaborn
• Scikit‑Learn


Modeling & Evaluation

• Train/Test Split, Cross‑Validation
• MAE, RMSE, R²
• Feature Importance & Coefficients


Deployment Considerations

• Low‑latency inference (<50ms)
• Sensor‑driven telemetry pipeline
• Simple validation schemas


Workflow

• Jupyter Notebooks
• GitHub Version Control
• VS Code


---

📌 Key Results

• 15% reduction in RMSE
• 10% lift in R²
• <50ms inference latency
• Fully interpretable model
• Stable across environmental fluctuations
• Ready for dashboard integration


---

🚀 Future Work & Operational Extensions

To maximize real‑time impact and plant reliability, the forecasting framework can be extended across three core pillars:

---

1. Model & Pipeline Architecture

• Advanced Modeling — Benchmark GBDT and Elastic Net.
• Feature Expansion — Add turbine load, fuel mix, diurnal cycles.
• Real‑Time Streaming Infrastructure — Deploy via Kafka + FastAPI.
• Model Governance & Drift Detection — Add automated drift checks (Evidently AI).


---

2. Operator Experience & Decision Support

• Interactive Dashboards — Real‑time forecasts, uncertainty bounds, maintenance recommendations.
• Scenario Engine — Simulate extreme environmental or operational conditions.


---

3. Real‑Time Explainability Layer

• Granular Feature Attribution — SHAP/LIME for per‑prediction breakdowns.
• Natural Language Narratives — Operator‑friendly explanations.
• Explainability‑Driven Audits & Alerts — Flag abnormal model reasoning.


---

📄 License

MIT License recommended.