import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle


df = pd.read_csv("loan_eligibility_data.csv")

# Features and target
X = df.drop(columns=['loan_eligible'])
y = df['loan_eligible']

# Train-test split with seed
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")

# Save the trained model to disk
with open('loan_eligibility_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model saved as 'loan_eligibility_model.pkl'")
