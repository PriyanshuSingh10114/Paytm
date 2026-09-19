import pandas as pd
import numpy as np
import json
import sys

# Configure stdout
sys.stdout.reconfigure(encoding='utf-8')

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
df['primary_app_clean'] = df['primary_app'].replace({'Google pay': 'Google Pay'})

# Fix encoding artifacts like 815 -> 8–15
def clean_text(val):
    if pd.isna(val):
        return val
    s = str(val)
    s = s.replace('\ufffd', '–').replace('', '–')
    return s

for c in df.columns:
    if df[c].dtype == 'object':
        df[c] = df[c].apply(clean_text)

# Let's inspect data quality
print(f"Total Rows: {len(df)}")
print(f"Total Nulls per column:\n{df.isnull().sum()}")
print(f"\nDuplicate rows across all columns: {df.duplicated().sum()}")
print(f"Duplicate rows excluding timestamp: {df.duplicated(subset=[c for c in df.columns if c != 'timestamp']).sum()}")

# Detailed verbatim inspection
verbatims_list = []
for idx, row in df.iterrows():
    verbatims_list.append({
        'id': idx + 1,
        'profile': row['profile'],
        'city': str(row['city']).strip(),
        'apps_used': row['apps_used'],
        'primary_app': row['primary_app_clean'],
        'paytm_90d': row['paytm_90d'],
        'weekly_freq': row['weekly_freq'],
        'top_occasions': row['top_occasions'],
        'primary_reason': row['primary_reason'],
        'paytm_occasions': row['paytm_occasions'],
        'paytm_barriers': row['paytm_barriers'],
        'trigger_verbatim': row['paytm_trigger_verbatim'],
        'open_followup': row['open_followup'],
        'contact': str(row['contact']) if pd.notna(row['contact']) else None
    })

with open('all_verbatims.json', 'w', encoding='utf-8') as f:
    json.dump(verbatims_list, f, indent=2, ensure_ascii=False)

print("Saved all_verbatims.json")
