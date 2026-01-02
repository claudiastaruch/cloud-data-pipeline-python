import pandas as pd
import glob
import os

# Path to the folder containing THIS script (graphs.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Get all raw CSVs (exclude any existing cleaned file)
# Go up one folder, then into Datasets
# Puts the strings together with / between
PATH = os.path.join(BASE_DIR, "..", "Datasets", "raw", "*.csv")
csv_files = glob.glob(PATH)
#csv_files = [f for f in csv_files if "cleaned_tobacco_data" not in f]

print("Files being combined:")
for f in csv_files:
    print(" -", f)

# 2. Combine all CSVs into one big dataframe
big_df = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)
print("Combined shape (before cleaning):", big_df.shape)

# 3. Copy and clean
df = big_df.copy()

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r'[^0-9a-zA-Z]+', '_', regex=True)
)

# Convert types
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["disparity_value"] = pd.to_numeric(df["disparity_value"], errors="coerce")

# Drop rows with missing year or disparity_value/ Rename column
df = df.rename(columns={
            "comparing_focus_group_": "focus_group",
            "cigarette_use_prevalence_focus_group_": "focus_prevalence",
            "cigarette_use_prevalence_reference_group_": "reference_prevalence"
})


# Drop rows with missing year or disparity_value
df = df.dropna(subset=["year", "disparity_value"])

print("Cleaned shape (after cleaning):", df.shape)

OUTPUT_PATH = os.path.join(BASE_DIR, "..", "Datasets", "cleaned", "cleaned_tobacco_data.csv")
df.to_csv(OUTPUT_PATH, index=False)
print("Saved cleaned_tobacco_data.csv")

###DATA CLEANING DONE