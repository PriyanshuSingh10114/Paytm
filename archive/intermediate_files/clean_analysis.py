import pandas as pd
import numpy as np
import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

# Read fresh from excel
df = pd.read_excel('Paytm UPI Growth Challenge 2026 — Raw Short VOC Responses.xlsx', sheet_name='Form Responses 1')
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
df['primary_app'] = df['primary_app'].replace({'Google pay': 'Google Pay'})
df['city_clean'] = df['city'].astype(str).str.strip().str.title()

# Fix encoding issues in strings
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].astype(str).str.replace('\ufffd', '–')

print(f"Total Rows: {len(df)}")

def parse_multi(series):
    items = []
    for val in series:
        if pd.isna(val) or val in ['None', 'nan', '']:
            continue
        parts = [p.strip() for p in str(val).split(',') if p.strip()]
        items.extend(parts)
    c = Counter(items)
    res = pd.DataFrame(c.most_common(), columns=['Item', 'Count'])
    res['Pct_of_Respondents'] = (res['Count'] / len(series) * 100).round(2)
    return res

print("\n--- 1. PROFILE BREAKDOWN (N=111) ---")
prof = df['profile'].value_counts()
prof_pct = (prof / len(df) * 100).round(2)
print(pd.DataFrame({'Count': prof, 'Percentage': prof_pct}))

print("\n--- 2. GEOGRAPHIC DISTRIBUTION (TOP CITIES) ---")
city_counts = df['city_clean'].value_counts()
print(city_counts.head(15))

print("\n--- 3. PRIMARY APP (N=111) ---")
pa = df['primary_app'].value_counts()
pa_pct = (pa / len(df) * 100).round(2)
print(pd.DataFrame({'Count': pa, 'Percentage': pa_pct}))

print("\n--- 4. PAYTM 90-DAY ACTIVITY (N=111) ---")
p90 = df['paytm_90d'].value_counts()
p90_pct = (p90 / len(df) * 100).round(2)
print(pd.DataFrame({'Count': p90, 'Percentage': p90_pct}))

print("\n--- 5. WEEKLY TRANSACTION FREQUENCY (N=111) ---")
wf = df['weekly_freq'].value_counts()
wf_pct = (wf / len(df) * 100).round(2)
print(pd.DataFrame({'Count': wf, 'Percentage': wf_pct}))

print("\n--- 6. APPS IN REPERTOIRE (MULTI-SELECT) ---")
print(parse_multi(df['apps_used']))

print("\n--- 7. TOP GENERAL UPI PAYMENT OCCASIONS (MULTI-SELECT) ---")
print(parse_multi(df['top_occasions']))

print("\n--- 8. WHY USERS CHOOSE PRIMARY APP (MULTI-SELECT) ---")
print(parse_multi(df['primary_reason']))

print("\n--- 9. WHEN USERS CURRENTLY USE PAYTM (MULTI-SELECT) ---")
print(parse_multi(df['paytm_occasions']))

print("\n--- 10. BIGGEST BARRIERS TO PAYTM (MULTI-SELECT) ---")
print(parse_multi(df['paytm_barriers']))

print("\n--- 11. IN-DEPTH FOLLOW-UP WILLINGNESS (N=111) ---")
fu = df['open_followup'].value_counts()
print(fu)
print(f"Contact provided count: {df['contact'].replace({'nan': np.nan, 'None': np.nan}).notna().sum()}")

# Save clean json
df.to_json('clean_voc_data.json', orient='records', indent=2, force_ascii=False)
print("\nSaved clean_voc_data.json successfully.")
