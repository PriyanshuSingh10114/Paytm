import pandas as pd
import numpy as np
import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open('all_verbatims.json', 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)

print("=== TOTAL RECORDS ===")
print(f"Total rows: {len(df)}")

# Fix encoding replacements in text
for col in ['weekly_freq', 'top_occasions', 'primary_reason', 'paytm_occasions', 'paytm_barriers']:
    df[col] = df[col].astype(str).str.replace('\ufffd', '–').str.replace('', '–')

print("\n=== 1. AUDIT & SAMPLE BREAKDOWN ===")
print("Profiles:")
print(df['profile'].value_counts())
print("\nCities (Top 15):")
print(df['city'].str.title().value_counts().head(15))

print("\nPrimary Apps:")
print(df['primary_app'].value_counts())

print("\nPaytm 90d usage:")
print(df['paytm_90d'].value_counts())

print("\nWeekly frequency:")
print(df['weekly_freq'].value_counts())

# Multi-select parsing helper
def get_multiselect_counts(series):
    items = []
    for val in series:
        if pd.isna(val) or val == 'None' or val == 'nan':
            continue
        # Split by comma or specific separator
        parts = [p.strip() for p in val.split(',') if p.strip()]
        items.extend(parts)
    return pd.Series(Counter(items)).sort_values(ascending=False)

print("\n=== TOP GENERAL UPI OCCASIONS ===")
occ_counts = get_multiselect_counts(df['top_occasions'])
print(occ_counts)
print("\nPercentage of respondents mentioning occasion (N=111):")
print((occ_counts / len(df) * 100).round(1))

print("\n=== PRIMARY APP SELECTION REASONS ===")
pri_reasons = get_multiselect_counts(df['primary_reason'])
print(pri_reasons)
print("\nPercentage mentioning reason:")
print((pri_reasons / len(df) * 100).round(1))

print("\n=== PAYTM OCCASIONS ===")
p_occ = get_multiselect_counts(df['paytm_occasions'])
print(p_occ)
print("\nPercentage mentioning Paytm occasion:")
print((p_occ / len(df) * 100).round(1))

print("\n=== PAYTM BARRIERS ===")
p_barr = get_multiselect_counts(df['paytm_barriers'])
print(p_barr)
print("\nPercentage mentioning barrier:")
print((p_barr / len(df) * 100).round(1))

# Cross tabs
print("\n=== PRIMARY APP vs PAYTM 90-DAY ACTIVE ===")
print(pd.crosstab(df['primary_app'], df['paytm_90d'], margins=True))

print("\n=== PRIMARY APP vs WEEKLY FREQ ===")
print(pd.crosstab(df['primary_app'], df['weekly_freq'], margins=True))

print("\n=== PROFILE vs PRIMARY APP ===")
print(pd.crosstab(df['profile'], df['primary_app'], margins=True))

print("\n=== PROFILE vs WEEKLY FREQ ===")
print(pd.crosstab(df['profile'], df['weekly_freq'], margins=True))

# Analyzing College Students vs Working Professionals
print("\n=== COLLEGE STUDENTS SUBSET (N=69) ===")
cs = df[df['profile'] == 'College student']
print("Primary Apps:", cs['primary_app'].value_counts().to_dict())
print("Paytm 90d:", cs['paytm_90d'].value_counts().to_dict())
print("Weekly Freq:", cs['weekly_freq'].value_counts().to_dict())
print("Top Occasions:", get_multiselect_counts(cs['top_occasions']).head(7).to_dict())
print("Barriers:", get_multiselect_counts(cs['paytm_barriers']).head(7).to_dict())

print("\n=== WORKING PROFESSIONALS SUBSET (N=23) ===")
wp = df[df['profile'] == 'Working professional']
print("Primary Apps:", wp['primary_app'].value_counts().to_dict())
print("Paytm 90d:", wp['paytm_90d'].value_counts().to_dict())
print("Weekly Freq:", wp['weekly_freq'].value_counts().to_dict())
print("Top Occasions:", get_multiselect_counts(wp['top_occasions']).head(7).to_dict())
print("Barriers:", get_multiselect_counts(wp['paytm_barriers']).head(7).to_dict())

