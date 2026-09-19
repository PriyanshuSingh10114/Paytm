import os
import shutil
import pandas as pd
import numpy as np
import json
from collections import Counter
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== STEP 1: INSPECTING & ORGANIZING PROJECT DIRECTORY ===")

base_dir = r"e:\Paytm"

# Folder Structure
dirs_to_create = [
    "data/raw",
    "data/cleaned",
    "data/final",
    "data/archive",
    "analysis/exploratory",
    "analysis/segmentation",
    "analysis/insights",
    "analysis/validation",
    "visualizations/geography",
    "visualizations/profession",
    "visualizations/demographics",
    "visualizations/payment_behaviour",
    "visualizations/app_preference",
    "visualizations/insights",
    "visualizations/final",
    "submission/executive_summary",
    "submission/supporting_evidence",
    "archive/duplicate_files",
    "archive/intermediate_files",
    "archive/unused_files"
]

for d in dirs_to_create:
    full_path = os.path.join(base_dir, d)
    os.makedirs(full_path, exist_ok=True)
    print(f"Ensured directory: {d}")

# Load and identify datasets
raw_excel = os.path.join(base_dir, "Paytm UPI Growth Challenge 2026 — Raw Short VOC Responses.xlsx")
trained_csv = os.path.join(base_dir, "Paytm_VOC_Trained_Dataset.csv")
trained_xlsx = os.path.join(base_dir, "Paytm_VOC_Trained_Dataset.xlsx")
virtus_cleaned = os.path.join(base_dir, "VIRTUS_113_RAW_CLEANED.xlsx")
virtus_voc_clean = os.path.join(base_dir, "VIRTUS_VOC_CLEAN.xlsx")

# Copy raw source to data/raw
shutil.copy2(raw_excel, os.path.join(base_dir, "data/raw", "Paytm_UPI_Raw_VOC_Responses.xlsx"))
shutil.copy2(trained_csv, os.path.join(base_dir, "data/cleaned", "Paytm_VOC_Trained_Dataset.csv"))
shutil.copy2(trained_xlsx, os.path.join(base_dir, "data/cleaned", "Paytm_VOC_Trained_Dataset.xlsx"))
shutil.copy2(virtus_cleaned, os.path.join(base_dir, "data/cleaned", "VIRTUS_113_RAW_CLEANED.xlsx"))
shutil.copy2(virtus_voc_clean, os.path.join(base_dir, "data/cleaned", "VIRTUS_VOC_CLEAN.xlsx"))

# Master dataset load
df = pd.read_csv(trained_csv)
print(f"\nLoaded Authoritative Dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# Standardize and enrich the final dataset
df_final = df.copy()

# City Standardization
city_map = {
    'Sitapur ': 'Sitapur', 'Sitapur': 'Sitapur',
    'Bhopal': 'Bhopal', 'Bhopal ': 'Bhopal', 'bhopal': 'Bhopal', 'BHOPAL ': 'Bhopal',
    'Lucknow ': 'Lucknow', 'Lucknow': 'Lucknow',
    'Lakhimpur Kheri ': 'Lakhimpur Kheri', 'Kheri': 'Lakhimpur Kheri', 'Lakhimapur Kheri': 'Lakhimpur Kheri',
    'Shahjahanpur ': 'Shahjahanpur', 'Biswan': 'Biswan',
    'Ballia': 'Ballia', 'Vallia': 'Ballia',
    'Sehore': 'Sehore',
    'Bangalore': 'Bengaluru',
    'Hardoi': 'Hardoi', 'Hardoi ': 'Hardoi',
    'Delhi': 'Delhi (NCR)', 'Noida': 'Noida',
    'Gurgaon ': 'Gurgaon', 'gurugram ': 'Gurgaon',
    'Agra ': 'Agra', 'Agra': 'Agra',
    'Dehradun': 'Dehradun', 'Panipat': 'Panipat', 'Karnal ': 'Karnal',
    'Shimla': 'Shimla', 'Surat': 'Surat', 'Pune': 'Pune',
    'Sangali Maharashtra ': 'Sangli', 'Indore': 'Indore',
    'Bhubaneswar ': 'Bhubaneswar', 'Jamshedpur ': 'Jamshedpur',
    'Mathura': 'Mathura', 'Hamirpur ': 'Hamirpur', 'Prayagraj': 'Prayagraj',
    'Akbarpur ': 'Akbarpur', 'Laharpur': 'Laharpur', 'Babhnan ': 'Babhnan',
    'Kotwara po kotwara': 'Kotwara', 'Gaura ': 'Gaura',
    'Uttar Pradesh ': 'Uttar Pradesh (General)', 'Uttar Pradesh': 'Uttar Pradesh (General)',
    'Rajsthan': 'Rajasthan (General)', 'Riga , Latvia ': 'Overseas / Student'
}

df_final['City_Standardized'] = df_final['2. Which city do you currently live in?'].map(city_map).fillna(df_final['2. Which city do you currently live in?'])

state_map = {
    'Sitapur': 'Uttar Pradesh', 'Lucknow': 'Uttar Pradesh', 'Lakhimpur Kheri': 'Uttar Pradesh',
    'Shahjahanpur': 'Uttar Pradesh', 'Biswan': 'Uttar Pradesh', 'Hardoi': 'Uttar Pradesh',
    'Ballia': 'Uttar Pradesh', 'Agra': 'Uttar Pradesh', 'Noida': 'Uttar Pradesh',
    'Mathura': 'Uttar Pradesh', 'Hamirpur': 'Uttar Pradesh', 'Prayagraj': 'Uttar Pradesh',
    'Akbarpur': 'Uttar Pradesh', 'Laharpur': 'Uttar Pradesh', 'Babhnan': 'Uttar Pradesh',
    'Kotwara': 'Uttar Pradesh', 'Gaura': 'Uttar Pradesh', 'Uttar Pradesh (General)': 'Uttar Pradesh',
    'Bhopal': 'Madhya Pradesh', 'Sehore': 'Madhya Pradesh', 'Indore': 'Madhya Pradesh',
    'Delhi (NCR)': 'Delhi (NCR)', 'Gurgaon': 'Haryana', 'Panipat': 'Haryana', 'Karnal': 'Haryana',
    'Bengaluru': 'Karnataka', 'Pune': 'Maharashtra', 'Sangli': 'Maharashtra', 'Surat': 'Gujarat',
    'Dehradun': 'Uttarakhand', 'Shimla': 'Himachal Pradesh', 'Bhubaneswar': 'Odisha',
    'Jamshedpur': 'Jharkhand', 'Rajasthan (General)': 'Rajasthan', 'Overseas / Student': 'Other / Overseas'
}

df_final['State_Standardized'] = df_final['City_Standardized'].map(state_map).fillna('Other')

# Settlement Typology
def get_settlement(city):
    c = str(city).lower()
    if any(x in c for x in ['bengaluru', 'bangalore', 'delhi', 'noida', 'gurgaon', 'gurugram', 'surat', 'pune', 'dehradun', 'shimla', 'lucknow', 'bhopal', 'bhubaneswar', 'indore']):
        return 'Urban Metros & State Capitals'
    else:
        return 'Tier-3 Towns, Semi-Urban & Rural Heartland'

df_final['Settlement_Typology'] = df_final['City_Standardized'].apply(get_settlement)

# Clean Primary App
df_final['Primary_App_Clean'] = df_final['4. Which UPI app do you use MOST?'].replace({'Google pay': 'Google Pay'}).str.strip()

# Frequency Category
def get_velocity(freq):
    f = str(freq)
    if '30+' in f or '16' in f:
        return 'High-Velocity (≥16 txns/wk | 65-130+ /mo)'
    elif '8' in f:
        return 'Regular (8-15 txns/wk | 32-64 /mo)'
    else:
        return 'Moderate/Occasional (1-7 txns/wk | 4-30 /mo)'

df_final['Transaction_Velocity'] = df_final['6. Roughly how many UPI payments do you make in a typical week?'].apply(get_velocity)

# Save Final Cleaned Dataset to data/final
final_csv = os.path.join(base_dir, "data/final", "Paytm_VOC_Authoritative_Final_Dataset.csv")
final_xlsx = os.path.join(base_dir, "data/final", "Paytm_VOC_Authoritative_Final_Dataset.xlsx")

df_final.to_csv(final_csv, index=False, encoding='utf-8')
df_final.to_excel(final_xlsx, index=False)
print(f"Saved Authoritative Final Dataset to: {final_csv}")

# Archive scratch scripts safely
scratch_files = [
    "clean_analysis.py", "cluster_utf8.py", "cluster_verbatims.py",
    "cross_analysis.py", "deep_dive.py", "dump_verbatims.py",
    "full_analysis.py", "inspect_all_verbatims.py", "run_cross.py",
    "scratch_analyze.py", "test_clean_geo.py", "verify_figures.py"
]

for sf in scratch_files:
    src = os.path.join(base_dir, sf)
    if os.path.exists(src):
        dst = os.path.join(base_dir, "archive/intermediate_files", sf)
        shutil.copy2(src, dst)
        print(f"Archived intermediate script: {sf}")

print("\nStep 1 completed successfully.")
