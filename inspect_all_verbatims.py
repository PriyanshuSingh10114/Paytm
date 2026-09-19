import json
import pandas as pd
from collections import Counter
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('clean_voc_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Let's inspect all 111 verbatims and categorize them
print("=== VERBATIM ANALYSIS ===")
verbatims = df[['profile', 'city_clean', 'primary_app', 'paytm_90d', 'weekly_freq', 'paytm_trigger_verbatim', 'paytm_barriers']].copy()

for i, r in verbatims.iterrows():
    print(f"[{i+1}] ({r['profile']}, {r['city_clean']}, Primary: {r['primary_app']}, Paytm90d: {r['paytm_90d']}, Freq: {r['weekly_freq']})")
    print(f"   Barriers: {r['paytm_barriers']}")
    print(f"   Verbatim: \"{r['paytm_trigger_verbatim']}\"")
    print("-" * 50)
