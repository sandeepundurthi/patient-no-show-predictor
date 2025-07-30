# 🏥 Patient No-Show Prediction using Machine Learning

Predicting whether patients will miss their medical appointments using real-world healthcare data. Built multiple machine learning and deep learning models to support proactive scheduling and reduce no-show rates.

---

## 📌 Project Overview

- **Goal**: Predict patient no-shows based on behavioral and demographic patterns
- **Dataset**: 110K+ real medical appointment records
- **Target Variable**: `Showed_up` (binary classification)
- **Tech Stack**: Python, Scikit-learn, XGBoost, TensorFlow/Keras, Matplotlib, Seaborn

---

## 📊 Exploratory Data Analysis (EDA)

- Analyzed gender, age, and health condition distributions
- Created a **waiting time** feature from `ScheduledDay` and `AppointmentDay`
- Key visualizations:
  - Gender-based no-show rates
  - KDE plots for age vs attendance
  - Correlation heatmaps and bar charts

---

## ⚙️ Feature Engineering & Selection

- Dropped irrelevant columns: IDs, raw timestamps, Neighbourhood
- Encoded categorical features (e.g., Gender: `F=0`, `M=1`)
- Selected top 5 features using `SelectKBest` with ANOVA F-test
- Applied `StandardScaler` for SVM and Neural Network models

---

## 🤖 Models Trained & Evaluated

| Model           | Accuracy | Recall (No-Show) | ROC AUC | Key Notes |
|------------------|----------|------------------|---------|-----------|
| Random Forest     | 77.1%    | 92%              | 0.67    | Good balance |
| SVM (RBF Kernel)  | 80.0%    | **100%**         | —       | Overpredicts no-shows |
| XGBoost           | 79.6%    | 98%              | **0.71**| Best AUC |
| Neural Network (Keras) | **80.0%** | ~95% | ~0.70 | Most stable, best accuracy |

> ✅ Final test accuracy (Neural Net): **80.04%**

---

## 📈 Performance Visualizations

- Confusion matrices for all models
- ROC curves with AUC scores
- Loss curve (training vs validation) for Neural Network

---

## 🧠 Key Learnings

- Importance of **recall for no-show** class in healthcare applications
- Trade-offs between **precision and recall** for different models
- Neural Network regularization with Dropout stabilized performance
- XGBoost had the **highest ROC AUC**, identifying high-risk patients effectively

---


