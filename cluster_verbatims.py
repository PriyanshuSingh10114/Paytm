import json
import pandas as pd
from collections import Counter
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('clean_voc_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def classify_verbatim(text):
    t = str(text).lower().strip()
    if t in ['na', 'no', 'n/a', 'none', 'nothing', 'nil', '-', '.', 'no need', 'not sure']:
        return 'No specific request / None / NA'
    
    categories = []
    if any(w in t for w in ['cashback', 'reward', 'offer', 'discount', 'points', 'coupon', 'money', 'free', 'rupees', 'rs', 'benefit', 'deals']):
        categories.append('Rewards / Cashback / Offers')
    if any(w in t for w in ['ui', 'ux', 'interface', 'clean', 'simple', 'fast', 'speed', 'smooth', 'lag', 'easy', 'glitch', 'hanging', 'clutter', 'ads', 'easy to use', 'simpler']):
        categories.append('Speed / UI / Simplicity / App Performance')
    if any(w in t for w in ['trust', 'security', 'secure', 'safe', 'privacy', 'scam', 'fraud', 'server', 'failed', 'failure', 'rbi', 'bank', 'reliable', 'reliability']):
        categories.append('Trust / Reliability / Server Success / Safety')
    if any(w in t for w in ['habit', 'default', 'use more', 'features', 'bill', 'recharge', 'credit', 'split', 'ticket', 'soundbox', 'merchant', 'accept', 'friend', 'convenien']):
        categories.append('Features / Ecosystem / Habit / Acceptance')
        
    if not categories:
        return 'Other / General'
    return ' + '.join(categories)

df['verbatim_theme'] = df['paytm_trigger_verbatim'].apply(classify_verbatim)

print("=== VERBATIM THEME DISTRIBUTION ===")
print(df['verbatim_theme'].value_counts())
print("\nPercentages:")
print((df['verbatim_theme'].value_counts() / len(df) * 100).round(2))

# Let's inspect individual themes and verbatim texts
for theme, group in df.groupby('verbatim_theme'):
    print(f"\n==================== THEME: {theme} (Count: {len(group)}) ====================")
    for idx, row in group.iterrows():
        print(f"Index {idx+1} | Profile: {row['profile']} | Primary: {row['primary_app']} | Paytm90d: {row['paytm_90d']} | Text: \"{row['paytm_trigger_verbatim']}\"")
