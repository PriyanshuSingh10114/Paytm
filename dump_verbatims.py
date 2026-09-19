import pandas as pd
import json

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

# Fix primary app casing
df['primary_app_clean'] = df['primary_app'].replace({'Google pay': 'Google Pay'})

# Cities
print("=== CITIES (TOP 20) ===")
print(df['city'].str.strip().str.title().value_counts().head(20))

print("\n=== ALL VERBATIMS (Column 11) ===")
for idx, row in df.iterrows():
    print(f"[{idx+1}] Profile: {row['profile']} | City: {row['city']} | Primary: {row['primary_app_clean']} | Paytm90d: {row['paytm_90d']} | Freq: {row['weekly_freq']} | Trigger: {row['paytm_trigger_verbatim']}")
