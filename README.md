# https-github.com-anshikagoel167-afk-Financial-Fraud
# 💳 AI-Based Financial Fraud Detection System

## 📌 Project Description

The **AI-Based Financial Fraud Detection System** is a Machine Learning project developed using Python to identify potentially fraudulent credit card transactions.

The system uses the **Logistic Regression** classification algorithm to analyze transaction data and classify transactions into two categories:

- **0 – Legitimate Transaction**
- **1 – Fraudulent Transaction**

The project uses a credit card transaction dataset and applies data preprocessing, feature scaling, and model training to detect suspicious transaction patterns. It also provides an interactive command-line feature that allows users to enter a transaction row number and check its predicted result.

## 🎯 Objectives

- Detect potentially fraudulent financial transactions using Machine Learning.
- Classify transactions as legitimate or fraudulent.
- Apply data preprocessing and feature scaling.
- Evaluate model performance using different classification metrics.
- Provide an interactive transaction prediction system.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Logistic Regression
- StandardScaler

## 📂 Dataset Information

The project uses a credit card transaction dataset (`creditcard.csv`).

The dataset contains the following features:

- `Time` – Time elapsed between transactions.
- `V1` to `V28` – Anonymized transaction features.
- `Amount` – Transaction amount.
- `Class` – Target variable (0 = Legitimate, 1 = Fraudulent).

## ⚙️ Machine Learning Workflow

1. Load the credit card transaction dataset.
2. Separate input features (X) and target labels (y).
3. Split the dataset into training (80%) and testing (20%) sets.
4. Apply StandardScaler for feature scaling.
5. Train the Logistic Regression model with balanced class weights.
6. Predict transaction classes.
7. Evaluate performance using accuracy, confusion matrix, precision, recall, and F1-score.
8. Allow users to check individual transactions through row-number input.

## 📊 Model Performance

The model achieved the following results on the test dataset:

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 97.55% |
| Fraud Precision | 0.06 |
| Fraud Recall | 0.92 |
| Fraud F1-Score | 0.11 |

**Note:** Due to class imbalance in the dataset, accuracy alone does not represent the complete model performance. The model achieves high fraud recall but has low fraud precision, resulting in a significant number of false-positive predictions.

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd FraudDetectionProject
```

### 3. Install Required Libraries

```bash
pip install pandas numpy scikit-learn
```

### 4. Add the Dataset

Place `creditcard.csv` in the same folder as `fraud_detection.py`.

### 5. Run the Python File

```bash
python fraud_detection.py
```

### 6. Check Transaction Predictions

Enter a row number when prompted:

```text
Enter row number OR type 'exit': 50
```

The system displays the predicted transaction category and the actual class from the dataset.

Type `exit` to close the program.

## 🔮 Future Scope

- Develop a graphical user interface using Streamlit or Flask.
- Improve fraud detection precision and reduce false positives.
- Experiment with algorithms such as Random Forest and Decision Tree.
- Integrate real-time transaction monitoring.
- Improve model performance through hyperparameter tuning.

## 👩‍💻 Developed By

**Anshika Goel**

B.Tech – Computer Science and Engineering

## 📌 Project Type

Academic Project | Machine Learning | Artificial Intelligence

---

**Disclaimer:** This project is developed for educational purposes. Its predictions are not intended to serve as a standalone financial fraud verification or prevention system.
