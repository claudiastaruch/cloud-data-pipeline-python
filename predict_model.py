import pandas as pd
import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'best_disparity_model.pkl')

def predict_smoking_disparity(year, demographic_type, focus_group):
    # Load model
    try:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    except Exception as e:
        return f"ERROR: Could not load model. Detail: {e}"

    # Prepare the feature row matching training structure
    try:
        X_new = pd.DataFrame(0, index=[0], columns=model.feature_names_in_)
    except Exception as e:
        return f"ERROR: Model is missing feature names. Detail: {e}"

    # Numeric feature
    X_new["year"] = year

    # One-hot demographic feature
    demo_col = f"demographic_{demographic_type}"
    if demographic_type != "Age":  # Age is base case
        if demo_col in X_new.columns:
            X_new[demo_col] = 1
        else:
            return f"ERROR: Demographic '{demographic_type}' not recognized."

    # One-hot focus group feature
    group_col = f"focus_group_{focus_group}"
    if group_col in X_new.columns:
        X_new[group_col] = 1
    else:
        return f"ERROR: Focus group '{focus_group}' not recognized."

    try:
        return float(model.predict(X_new)[0])
    except Exception as e:
        return f"ERROR: Prediction failed. Detail: {e}"
