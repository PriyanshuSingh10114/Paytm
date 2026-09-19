import json
import pandas as pd
import numpy as np

with open('clean_voc_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Let's verify exact metrics for all sections
print("--- AUDIT NUMBERS ---")
print("Total rows:", len(df))
print("Unique rows:", len(df.drop_duplicates()))
print("Missing values in survey fields:", df.drop(columns=['contact']).isnull().sum().sum())
print("Open to follow-up (Yes):", (df['open_followup'] == 'Yes').sum(), f"({(df['open_followup'] == 'Yes').mean()*100:.2f}%)")
print("Open to follow-up (No):", (df['open_followup'] == 'No').sum(), f"({(df['open_followup'] == 'No').mean()*100:.2f}%)")
print("Valid contacts provided:", df['contact'].replace({'nan': np.nan, 'None': np.nan}).notna().sum())

# Profile
print("\n--- PROFILES ---")
for k, v in df['profile'].value_counts().items():
    print(f"{k}: {v} ({v/len(df)*100:.2f}%)")

# Primary app
print("\n--- PRIMARY APPS ---")
for k, v in df['primary_app'].value_counts().items():
    print(f"{k}: {v} ({v/len(df)*100:.2f}%)")

# Paytm 90d
print("\n--- PAYTM 90D ---")
for k, v in df['paytm_90d'].value_counts().items():
    print(f"{k}: {v} ({v/len(df)*100:.2f}%)")

# Weekly freq
print("\n--- WEEKLY FREQ ---")
for k, v in df['weekly_freq'].value_counts().items():
    print(f"{k}: {v} ({v/len(df)*100:.2f}%)")

# High frequency
high_freq_mask = df['weekly_freq'].isin(['16–30', '30+'])
print(f"High Freq (16+ txns/wk): {high_freq_mask.sum()} ({high_freq_mask.mean()*100:.2f}%)")

# College student high freq
cs_mask = df['profile'] == 'College student'
cs_high_freq = cs_mask & high_freq_mask
print(f"College students high freq: {cs_high_freq.sum()} / {cs_mask.sum()} ({cs_high_freq.sum()/cs_mask.sum()*100:.2f}%)")

# Non Paytm Primary but Paytm 90d active
non_paytm_mask = df['primary_app'] != 'Paytm'
non_paytm_active = non_paytm_mask & (df['paytm_90d'] == 'Yes')
print(f"Non-Paytm Primary total: {non_paytm_mask.sum()} ({non_paytm_mask.mean()*100:.2f}%)")
print(f"Non-Paytm Primary but Paytm 90d active: {non_paytm_active.sum()} / {non_paytm_mask.sum()} ({non_paytm_active.sum()/non_paytm_mask.sum()*100:.2f}%)")
print(f"Percentage of total sample who have Paytm active but default to rival: {non_paytm_active.sum()} / {len(df)} ({non_paytm_active.sum()/len(df)*100:.2f}%)")

