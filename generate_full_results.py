import json
import pandas as pd
import numpy as np
from collections import Counter
import sys
import os

# Set stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

excel_path = 'Paytm UPI Growth Challenge 2026 — Raw Short VOC Responses.xlsx'
df = pd.read_excel(excel_path, sheet_name='Form Responses 1')

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
df['primary_app_clean'] = df['primary_app'].replace({'Google pay': 'Google Pay'}).str.strip()
df['city_clean'] = df['city'].astype(str).str.strip().str.title()

# Fix encoding issues in text
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].astype(str).str.replace('\ufffd', '–')

def parse_multiselect(series):
    items = []
    for val in series:
        if pd.isna(val) or val in ['None', 'nan', '']:
            continue
        parts = [p.strip() for p in str(val).split(',') if p.strip()]
        items.extend(parts)
    c = Counter(items)
    res = []
    for k, v in c.most_common():
        res.append({
            'item': k,
            'count': v,
            'percentage_of_respondents': round((v / len(series)) * 100, 2)
        })
    return res

# 1. High-level dataset stats
total_records = len(df)
unique_records = len(df.drop_duplicates())
missing_fields = int(df.drop(columns=['contact']).isnull().sum().sum())
followup_yes = int((df['open_followup'] == 'Yes').sum())
followup_yes_pct = round((followup_yes / total_records) * 100, 2)
valid_contacts = int(df['contact'].replace({'nan': np.nan, 'None': np.nan}).notna().sum())

# 2. Profile distribution
profile_counts = df['profile'].value_counts()
profiles_data = []
for k, v in profile_counts.items():
    profiles_data.append({
        'profile': k,
        'count': int(v),
        'percentage': round((v / total_records) * 100, 2)
    })

# 3. Primary App share
app_counts = df['primary_app_clean'].value_counts()
apps_data = []
for k, v in app_counts.items():
    apps_data.append({
        'app': k,
        'count': int(v),
        'percentage': round((v / total_records) * 100, 2)
    })

# 4. Paytm 90d usage
p90_counts = df['paytm_90d'].value_counts()
p90_data = []
for k, v in p90_counts.items():
    p90_data.append({
        'used_paytm_last_90d': k,
        'count': int(v),
        'percentage': round((v / total_records) * 100, 2)
    })

# 5. Weekly frequency
wf_counts = df['weekly_freq'].value_counts()
wf_data = []
for k, v in wf_counts.items():
    wf_data.append({
        'weekly_transactions': k,
        'count': int(v),
        'percentage': round((v / total_records) * 100, 2)
    })

# 6. Multi-select distributions
app_repertoire = parse_multiselect(df['apps_used'])
top_occasions = parse_multiselect(df['top_occasions'])
primary_reasons = parse_multiselect(df['primary_reason'])
paytm_occasions = parse_multiselect(df['paytm_occasions'])
paytm_barriers = parse_multiselect(df['paytm_barriers'])

# 7. Cross tabulations
# A: Non-Paytm Primary but Paytm 90d active
non_paytm_df = df[df['primary_app_clean'] != 'Paytm']
non_paytm_p90_active = int((non_paytm_df['paytm_90d'] == 'Yes').sum())
non_paytm_p90_active_pct = round((non_paytm_p90_active / len(non_paytm_df)) * 100, 2)

# B: High frequency (16+ txns/wk)
high_freq_df = df[df['weekly_freq'].isin(['16–30', '30+'])]
high_freq_count = len(high_freq_df)
high_freq_pct = round((high_freq_count / total_records) * 100, 2)

# C: Primary App x Paytm 90d
crosstab_app_p90 = pd.crosstab(df['primary_app_clean'], df['paytm_90d']).to_dict(orient='index')

# D: Profile x Primary App
crosstab_prof_app = pd.crosstab(df['profile'], df['primary_app_clean']).to_dict(orient='index')

# E: City Top 10
city_counts = df['city_clean'].value_counts().head(10)
city_data = [{'city': k, 'count': int(v), 'percentage': round((v / total_records) * 100, 2)} for k, v in city_counts.items()]

results = {
    'summary': {
        'total_responses': total_records,
        'unique_respondents': unique_records,
        'missing_fields': missing_fields,
        'open_to_followup_yes_count': followup_yes,
        'open_to_followup_yes_pct': followup_yes_pct,
        'valid_contacts_provided': valid_contacts,
        'paytm_primary_share_pct': round((int(app_counts.get('Paytm', 0)) / total_records) * 100, 2),
        'paytm_90d_active_reach_pct': round((int(p90_counts.get('Yes', 0)) / total_records) * 100, 2),
        'non_paytm_primary_90d_active_count': non_paytm_p90_active,
        'non_paytm_primary_90d_active_pct': non_paytm_p90_active_pct,
        'high_frequency_users_16plus_wk_pct': high_freq_pct
    },
    'profile_distribution': profiles_data,
    'primary_app_distribution': apps_data,
    'paytm_90d_activity': p90_data,
    'weekly_frequency_distribution': wf_data,
    'top_cities': city_data,
    'app_repertoire_mentions': app_repertoire,
    'top_payment_occasions': top_occasions,
    'primary_app_selection_reasons': primary_reasons,
    'paytm_current_occasions': paytm_occasions,
    'paytm_barriers_identified': paytm_barriers,
    'crosstabs': {
        'primary_app_vs_paytm_90d': crosstab_app_p90,
        'profile_vs_primary_app': crosstab_prof_app
    }
}

with open('dataset_results_and_outcomes.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("SUCCESS: dataset_results_and_outcomes.json generated successfully.")
print("\n=== SUMMARY OF KEY FINDINGS ===")
print(f"Total Respondents: {total_records}")
print(f"Paytm 90-day Active Reach: {p90_counts.get('Yes', 0)} / {total_records} ({results['summary']['paytm_90d_active_reach_pct']}%)")
print(f"Paytm Primary App Share: {app_counts.get('Paytm', 0)} / {total_records} ({results['summary']['paytm_primary_share_pct']}%)")
print(f"Non-Paytm Primary who are 90d Active on Paytm: {non_paytm_p90_active} / {len(non_paytm_df)} ({non_paytm_p90_active_pct}%)")
print(f"High Frequency Users (16+ txns/week): {high_freq_count} / {total_records} ({high_freq_pct}%)")
