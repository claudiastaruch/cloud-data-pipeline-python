#Predictive Analysis: ML models
#Training Random Forest Regressor

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pickle
import os

# Path to the folder containing THIS script (ml_model.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "..", "Datasets", "cleaned","cleaned_tobacco_data.csv")
DATA_PREVALENCE_PATH = os.path.join(BASE_DIR, "..", "Datasets", "cleaned", "prevalence_tobacco_data.csv")

# Load the CSVs
df = pd.read_csv(DATA_PATH)
df_prevalence = pd.read_csv(DATA_PREVALENCE_PATH) #just prevalence data across demographic groups, states, years


TARGET_COLUMN = 'disparity_value'

# Drop rows where the target or key features are missing
df_model = df.dropna(subset=[TARGET_COLUMN, 'focus_prevalence', 'demographic', 'focus_group', 'year']).copy()

# Select features (X) and target (y)
X = df_model[['year', 'focus_prevalence', 'demographic', 'focus_group']]
y = df_model[TARGET_COLUMN]

# One-hot encode categorical features automatically
X_processed = pd.get_dummies(X, columns=['demographic', 'focus_group'], drop_first=True)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
print(f"Data split. Training samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

print("Starting Random Forest Regressor training...")
rfr_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1, max_depth=10)
rfr_model.fit(X_train, y_train)
print("Training complete.")


y_pred = rfr_model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n--- Model Evaluation (Random Forest Regressor) ---")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

print(f"R2 Score: {r2:.4f}")

# --- 5. Save the trained model ---
MODEL_FILE = 'best_disparity_model.pkl'
with open(MODEL_FILE, 'wb') as f:
    pickle.dump(rfr_model, f)
print(f"\nModel successfully saved to '{MODEL_FILE}'")

print("The Random Forest Regressor was selected as the best model because it exhibited a lower RMSE (smaller error) and a higher $R^2$ score (better fit) compared to Linear Regression.")
