import json
import pandas as pd
import numpy as np
from collections import Counter
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('clean_voc_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def parse_multi_series(series):
    items = []
    for val in series:
        if pd.isna(val) or val in ['None', 'nan', '']:
            continue
        parts = [p.strip() for p in str(val).split(',') if p.strip()]
        items.extend(parts)
    return Counter(items)

print("=================================================================")
print("=== 1. PRIMARY REASON BY PRIMARY APP ===")
print("=================================================================")
for app in ['Google Pay', 'PhonePe', 'Paytm']:
    sub = df[df['primary_app'] == app]
    counts = parse_multi_series(sub['primary_reason'])
    print(f"\n--- Primary App: {app} (N={len(sub)}) ---")
    for k, v in counts.most_common():
        pct = (v / len(sub)) * 100
        print(f"  {k}: {v} ({pct:.1f}%)")

print("\n=================================================================")
print("=== 2. TOP UPI OCCASIONS BY PRIMARY APP ===")
print("=================================================================")
for app in ['Google Pay', 'PhonePe', 'Paytm']:
    sub = df[df['primary_app'] == app]
    counts = parse_multi_series(sub['top_occasions'])
    print(f"\n--- Primary App: {app} (N={len(sub)}) ---")
    for k, v in counts.most_common():
        pct = (v / len(sub)) * 100
        print(f"  {k}: {v} ({pct:.1f}%)")

print("\n=================================================================")
print("=== 3. PAYTM BARRIERS BY PRIMARY APP ===")
print("=================================================================")
for app in ['Google Pay', 'PhonePe', 'Paytm']:
    sub = df[df['primary_app'] == app]
    counts = parse_multi_series(sub['paytm_barriers'])
    print(f"\n--- Primary App: {app} (N={len(sub)}) ---")
    for k, v in counts.most_common():
        pct = (v / len(sub)) * 100
        print(f"  {k}: {v} ({pct:.1f}%)")

print("\n=================================================================")
print("=== 4. WHEN USERS USE PAYTM BY PRIMARY APP ===")
print("=================================================================")
for app in ['Google Pay', 'PhonePe', 'Paytm']:
    sub = df[df['primary_app'] == app]
    counts = parse_multi_series(sub['paytm_occasions'])
    print(f"\n--- Primary App: {app} (N={len(sub)}) ---")
    for k, v in counts.most_common():
        pct = (v / len(sub)) * 100
        print(f"  {k}: {v} ({pct:.1f}%)")

print("\n=================================================================")
print("=== 5. PAYTM 90-DAY USAGE AMONG NON-PAYTM PRIMARY USERS ===")
print("=================================================================")
non_paytm = df[df['primary_app'] != 'Paytm']
print(f"Total Non-Paytm Primary users: {len(non_paytm)} ({len(non_paytm)/len(df)*100:.1f}%)")
print(non_paytm['paytm_90d'].value_counts())
print(f"Paytm 90-day active among Non-Paytm Primary: {non_paytm['paytm_90d'].value_counts()['Yes']} / {len(non_paytm)} ({non_paytm['paytm_90d'].value_counts(normalize=True)['Yes']*100:.1f}%)")

print("\n=================================================================")
print("=== 6. HIGH-FREQUENCY SEGMENT (16-30, 30+ TXNS/WEEK) ===")
print("=================================================================")
high_freq = df[df['weekly_freq'].isin(['16–30', '30+'])]
print(f"High-frequency users: {len(high_freq)} ({len(high_freq)/len(df)*100:.1f}%)")
print("Primary Apps in High Freq:")
print(high_freq['primary_app'].value_counts())
print("\nPaytm 90d active in High Freq:")
print(high_freq['paytm_90d'].value_counts())
print("\nTop Occasions in High Freq:")
for k, v in parse_multi_series(high_freq['top_occasions']).most_common(8):
    print(f"  {k}: {v} ({v/len(high_freq)*100:.1f}%)")
print("\nBarriers in High Freq:")
for k, v in parse_multi_series(high_freq['paytm_barriers']).most_common(8):
    print(f"  {k}: {v} ({v/len(high_freq)*100:.1f}%)")

