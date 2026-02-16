import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

print("Loading data...")
try:
    X_train = pd.read_pickle("X_train_final.pkl")
    y_train = pd.read_pickle("y_train.pkl")
    
    # Ensure y_train is 1D array as expected by sklearn (series is also fine, but let's be safe)
    if isinstance(y_train, pd.DataFrame):
        y_train = y_train.squeeze()
        
    print(f"X_train shape: {X_train.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"X_train dtypes:\n{X_train.dtypes.value_counts()}")

    print("Fitting Logistic Regression...")
    model = LogisticRegression(max_iter=100) # Default max_iter
    model.fit(X_train, y_train)
    print("SUCCESS: Model fitted successfully.")
    
except Exception as e:
    print(f"FAILURE: Model fitting failed with error: {e}")
    # Print sample of data to debug if it fails
    # print(X_train.head())
