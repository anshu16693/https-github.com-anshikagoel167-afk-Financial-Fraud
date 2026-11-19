# 💳 AI-Based Financial Fraud Detection System
# Fixed Version

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# --- Step 1: Load Dataset ---
data = pd.read_csv("creditcard.csv")

# --- Step 2: Data Preprocessing ---
X = data.drop("Class", axis=1)
y = data["Class"]

# 🔥 IMPORTANT: Stratified split (maintains fraud ratio)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 🔥 Scale AFTER split (correct practice)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --- Step 3: Train Model ---
# 🔥 MAIN FIX: Handle imbalance
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# --- Step 4: Test Model ---
y_pred = model.predict(X_test)

# --- Step 5: Evaluate Model ---
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# --- Step 6: Custom Input Prediction ---
def check_fraud():
    while True:
        choice = input("\nEnter row number OR type 'exit': ")

        if choice.lower() == 'exit':
            print("\n👋 Exiting Fraud Detection System. Goodbye!\n")
            break

        try:
            row = int(choice)

            # Get raw values
            values = X.iloc[row].values.reshape(1, -1)

            # Scale using trained scaler
            values_scaled = scaler.transform(values)

            result = model.predict(values_scaled)

            print(f"\nRow {row} Actual Class:", y.iloc[row])

            if result[0] == 1:
                print("🚨 Fraudulent Transaction Detected!")
            else:
                print("✅ Legitimate Transaction")

        except Exception as e:
            print("❌ Invalid input. Try again.")
            print("Error:", e)

# Run system
check_fraud()
