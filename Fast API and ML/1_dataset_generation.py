import numpy as np
import pandas as pd

np.random.seed(42)  # for reproducibility

n = 1000

# Features
age = np.random.randint(21, 60, size=n)  # Age between 21 and 60
income = np.random.normal(50000, 15000, size=n).astype(int)  # Annual income around 50k
loan_amount = np.random.normal(15000, 7000, size=n).astype(int)  # Loan amount requested
credit_score = np.random.randint(300, 850, size=n)  # Credit score range
years_employed = np.random.randint(0, 20, size=n)  # Years employed
has_defaulted_before = np.random.choice([0, 1], size=n, p=[0.85, 0.15])  # 15% default history

# Target variable - Loan Eligibility (0 = No, 1 = Yes)
# Simple rule for eligibility for example:
# Eligible if income > 40k, credit_score > 600, no default before, and loan_amount < 30k
eligible = ((income > 40000) & (credit_score > 600) & (has_defaulted_before == 0) & (loan_amount < 30000)).astype(int)

# Create DataFrame
df = pd.DataFrame({
    'age': age,
    'income': income,
    'loan_amount': loan_amount,
    'credit_score': credit_score,
    'years_employed': years_employed,
    'has_defaulted_before': has_defaulted_before,
    'loan_eligible': eligible
})

# Clean up possible negative loan_amounts or incomes due to normal dist tail
df['loan_amount'] = df['loan_amount'].apply(lambda x: max(x, 1000))
df['income'] = df['income'].apply(lambda x: max(x, 10000))

print(df.head())

# Save to CSV
df.to_csv('loan_eligibility_data.csv', index=False)
