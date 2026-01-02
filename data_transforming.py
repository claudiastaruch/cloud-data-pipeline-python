import pandas as pd
#import glob
import os


#this file is to create the prevalence data frame in prevalence_tobacco_data.csv

# Path to the folder containing THIS script (graphs.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one folder, then into Datasets
# Puts the strings together with / between
DATA_PATH = os.path.join(BASE_DIR, "..", "Datasets", "cleaned", "cleaned_tobacco_data.csv")

# Load the CSV
df = pd.read_csv(DATA_PATH)

# Copy and clean
df_temp = df.copy()

# Clean column names
df_temp.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r'[^0-9a-zA-Z]+', '_', regex=True)
    .str.replace('_$', '', regex=True) #remove _ at the end of col names
)

# Convert types
df_temp["year"] = pd.to_numeric(df_temp["year"], errors="coerce")
df_temp["disparity_value"] = pd.to_numeric(df_temp["disparity_value"], errors="coerce")
df_temp = df_temp.rename(columns={"comparing_focus_group": "focus_group"})

# Drop rows with missing year or disparity_value
df_temp = df_temp.dropna(subset=["year", "disparity_value"])

#remove other columns and drop duplicate rows
df_temp = df_temp.drop(columns=["disparity_value", "to_reference_group", "reference_prevalence"]).drop_duplicates()

#copy data back to the original df
df = df_temp.copy()

print("Cleaned shape (after transformation):", df.shape)

OUTPUT_PATH = os.path.join(BASE_DIR, "..", "Datasets", "cleaned", "prevalence_tobacco_data.csv")
df.to_csv(OUTPUT_PATH, index=False)
print("Saved prevalence_tobacco_data.csv")

###DATA TRANSFORMATION DONE