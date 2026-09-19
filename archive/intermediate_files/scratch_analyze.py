import pandas as pd
import numpy as np
import json

# Load dataset
df = pd.read_excel('Paytm UPI Growth Challenge 2026 — Raw Short VOC Responses.xlsx', sheet_name='Form Responses 1')

print(f"Total Rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")

# Basic stats
col_map = {
    'Timestamp': 'timestamp',
    '1. Which best describes you?': 'profile',
    '2. Which city do you currently live in?': 'city',
    '3. Which UPI apps do you currently use?': 'apps_used',
    '4. Which UPI app do you use MOST?': 'primary_app',
    '5. Have you used Paytm UPI in the last 90 days?': 'paytm_90d',
    '6. Roughly how many UPI payments do you make in a typical week?': 'weekly_freq',
    '7. Where do you use UPI MOST often?': 'top_occasions',
    '8. What is the BIGGEST reason you usually open your primary UPI app?': 'primary_reason',
    '9. When are you MOST likely to use Paytm UPI?': 'paytm_occasions',
    '10. What is the BIGGEST reason you do NOT use Paytm for more of your UPI payments?': 'paytm_barriers',
    '11. In ONE sentence: what would make you use Paytm more?': 'paytm_trigger_verbatim',
    '12. Would you be open to a 15-minute follow-up conversation about your UPI habits?': 'open_followup',
    '13. If yes, please share your preferred contact (phone/email).': 'contact'
}

df = df.rename(columns=col_map)

# Clean city names
df['city_clean'] = df['city'].astype(str).str.strip().str.title()

# Summary analysis
print("\n--- 1. PROFILE BREAKDOWN ---")
print(df['profile'].value_counts(dropna=False))
print(df['profile'].value_counts(normalize=True)*100)

print("\n--- 2. PRIMARY APP BREAKDOWN ---")
print(df['primary_app'].value_counts(dropna=False))
print(df['primary_app'].value_counts(normalize=True)*100)

print("\n--- 3. PAYTM 90-DAY USAGE ---")
print(df['paytm_90d'].value_counts(dropna=False))
print(df['paytm_90d'].value_counts(normalize=True)*100)

print("\n--- 4. WEEKLY TRANSACTION FREQUENCY ---")
print(df['weekly_freq'].value_counts(dropna=False))
print(df['weekly_freq'].value_counts(normalize=True)*100)

print("\n--- 5. OPEN TO FOLLOW-UP (IN-DEPTH CANDIDATES) ---")
print(df['open_followup'].value_counts(dropna=False))
print(f"Total with contact provided: {df['contact'].notna().sum()}")

# Cross tabs
print("\n--- 6. PRIMARY APP BY PROFILE ---")
print(pd.crosstab(df['profile'], df['primary_app'], margins=True))

print("\n--- 7. PRIMARY APP BY PAYTM 90D USAGE ---")
print(pd.crosstab(df['primary_app'], df['paytm_90d'], margins=True))

print("\n--- 8. WEEKLY FREQ BY PRIMARY APP ---")
print(pd.crosstab(df['primary_app'], df['weekly_freq'], margins=True))

# Analysis of multi-select fields:
def explode_multiselect(series):
    return series.dropna().str.split(r',\s*|;|\n').explode().str.strip()

print("\n--- 9. ALL APPS USED ---")
all_apps = explode_multiselect(df['apps_used'])
print(all_apps.value_counts())

print("\n--- 10. TOP UPI OCCASIONS (ALL) ---")
all_occasions = explode_multiselect(df['top_occasions'])
print(all_occasions.value_counts())

print("\n--- 11. PRIMARY APP REASONS ---")
all_reasons = explode_multiselect(df['primary_reason'])
print(all_reasons.value_counts())

print("\n--- 12. WHEN LIKELY TO USE PAYTM ---")
paytm_occ = explode_multiselect(df['paytm_occasions'])
print(paytm_occ.value_counts())

print("\n--- 13. PAYTM BARRIERS ---")
barriers = explode_multiselect(df['paytm_barriers'])
print(barriers.value_counts())

# Save parsed data to JSON for detailed inspection
df.to_json('parsed_voc.json', orient='records', indent=2)
print("\nSaved parsed_voc.json successfully.")
