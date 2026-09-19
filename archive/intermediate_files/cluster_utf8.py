import json
import pandas as pd
from collections import Counter
import re
import sys

with open('clean_voc_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def classify_verbatim(text):
    t = str(text).lower().strip()
    if t in ['na', 'no', 'n/a', 'none', 'nothing', 'nil', '-', '.', 'no need', 'not sure', "i'm not a paytm user"]:
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

output_lines = []
output_lines.append("=== VERBATIM THEME DISTRIBUTION ===")
output_lines.append(str(df['verbatim_theme'].value_counts()))
output_lines.append("\nPercentages:")
output_lines.append(str((df['verbatim_theme'].value_counts() / len(df) * 100).round(2)))

for theme, group in df.groupby('verbatim_theme'):
    output_lines.append(f"\n==================== THEME: {theme} (Count: {len(group)}) ====================")
    for idx, row in group.iterrows():
        output_lines.append(f"Index {idx+1} | Profile: {row['profile']} | Primary: {row['primary_app']} | Paytm90d: {row['paytm_90d']} | Text: \"{row['paytm_trigger_verbatim']}\"")

with open('verbatim_clusters_utf8.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("Saved verbatim_clusters_utf8.txt")
