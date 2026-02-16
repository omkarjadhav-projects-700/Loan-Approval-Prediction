import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load Data
print("Loading data...")
try:
    df = pd.read_csv("preprocessed_data.csv")
except FileNotFoundError:
    print("Error: preprocessed_data.csv not found.")
    exit(1)

# 2. Manual Encoding (Mapping)
print("Encoding categorical variables...")

# Define mappings
health_insurance_map = {"Insured": 1, "Uninsured": 0}
life_insurance_map = {"Insured": 1, "Uninsured": 0}
car_insurance_map = {"Insured": 1, "Uninsured": 0}
home_insurance_map = {"Insured": 1, "Uninsured": 0}
education_level_map = {
    'High School': 1,
    'Associate': 2,
    'Bachelor': 3,
    'Master': 4,
    'Doctorate': 5
}

# Apply mappings
# Fill NaNs if necessary, though 'preprocessed_data.csv' suggests it might be clean. 
# Using map can introduce NaNs if keys are missing, so we should be careful.
# The original notebook didn't handle NaNs explicitly after mapping, assuming data quality.
# Define mappings
health_insurance_map = {"Insured": 1, "Uninsured": 0}
life_insurance_map = {"Insured": 1, "Uninsured": 0}
car_insurance_map = {"Insured": 1, "Uninsured": 0}
home_insurance_map = {"Insured": 1, "Uninsured": 0}
education_level_map = {
    'High School': 1,
    'Associate': 2,
    'Bachelor': 3,
    'Master': 4,
    'Doctorate': 5
}

# Apply mappings
df["HealthInsuranceStatus"] = df["HealthInsuranceStatus"].map(health_insurance_map)
df["LifeInsuranceStatus"] = df["LifeInsuranceStatus"].map(life_insurance_map)
df["CarInsuranceStatus"] = df["CarInsuranceStatus"].map(car_insurance_map)
df["HomeInsuranceStatus"] = df["HomeInsuranceStatus"].map(home_insurance_map)
df["EducationLevel"] = df["EducationLevel"].map(education_level_map)    

# 3. One-Hot Encoding
# The original notebook used get_dummies on specific columns: 
# ["LoanPurpose", "HomeOwnershipStatus", "EmploymentStatus", "MaritalStatus", "EmployerType"]
# Note: "EducationLevel" was in the get_dummies list in the original notebook cell 39/41 
# BUT it was also manually mapped in cell 31. 
# If we map it to integers first, get_dummies might not treat it as categorical unless specified.
# However, the original notebook cell 39 *included* "EducationLevel" in columns=... 
# This implies the user *might* have wanted it one-hot encoded OR ordinal encoded. 
# Given cell 31 does ordinal encoding (1-5), doing one-hot encoding *after* would be valid if it was still object,
# but since it's now int64, get_dummies(columns=[...]) might skip it or treat it as discrete.
# Let's look at the original code behavior:
# Cell 31 maps it. df["EducationLevel"] becomes int.
# Cell 39 calls get_dummies(..., columns=[..., "EducationLevel"], dtype=int).
# If it's int, get_dummies will OHE it if passed in 'columns'. 
# Usually, for ordinal variables like Education, we keep the ordinal encoding (1-5) and DO NOT One-Hot Encode. 
# OHE destroys the ordinal relationship.
# I will stick to the Ordinal Encoding for EducationLevel and REMOVE it from OHE to be safe and logical,
# UNLESS the original intention was purely OHE. 
# The original code did BOTH (mapped it, then OHE'd it via the blind `pd.get_dummies(df)` reset).
# I will assume Ordinal Encoding is the *better* choice for EducationLevel and SKIP OHE for it.

cols_to_ohe = ["LoanPurpose", "HomeOwnershipStatus", "EmploymentStatus", "MaritalStatus", "EmployerType"]
print(f"One-hot encoding columns: {cols_to_ohe}")
df = pd.get_dummies(df, columns=cols_to_ohe, drop_first=True, dtype=int)


# 4. Prepare X and y
print("Preparing X and y...")
X = df.drop("LoanApproved", axis=1)
y = df["LoanApproved"]

# 5. Split Data
print("Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

# 6. Scaling
print("Scaling features...")
scaler = StandardScaler()

# Identify columns to scale - usually all numerical columns. 
# The new boolean/int columns from OHE and manual mapping are technically numerical now.
# Scaling 0/1 dummies is debated but standard in many pipelines (like this notebook's attempt).
# I will simply scale X_train and X_test entirely.
# The original notebook specified a huge list of columns to scale. 
# It's safer to map columns to scale to ensure we don't miss any.
cols_to_scale = X_train.columns
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=cols_to_scale)
X_test = pd.DataFrame(scaler.transform(X_test), columns=cols_to_scale)



# Scale target (if regression? This is classification 'LoanApproved' 0/1). 
# Logistic Regression expects y to be class labels, NOT scaled floats usually.
# However, the original notebook cell 16 did `y_train = scaler.fit_transform([y_train])`.
# Scaling target for CLASSIFICATION (0/1) is WRONG. It turns 0/1 into floats like -0.5/0.5 or similar.
# LogisticRegression in sklearn expects integer labels or probability estimates.
# I will SKIP scaling y. If they really want it, I can add it, but it's likely an error.
# Wait, I see `y_train = scaler.fit_transform([y_train])` in the notebook.
# This actually produces a shape error/warning often, or creates a 2D array.
# The `LogisticRegression` fit call in cell 12 failed on X, not y (yet). 
# Standard practice: Do NOT scale targets for classification. I will enforce this best practice.

# 7. Save Data
print("Saving final datasets...")
X_train.to_pickle("X_train_final.pkl")
X_test.to_pickle("X_test_final.pkl")
y_train.to_pickle("y_train.pkl")
y_test.to_pickle("y_test.pkl")

print("Done. Files generated:")
print(" - X_train_final.pkl")
print(" - X_test_final.pkl")
print(" - y_train.pkl")
print(" - y_test.pkl")
