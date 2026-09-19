import os
import shutil
import json
import pandas as pd

base_dir = r"e:\Paytm"
final_csv = os.path.join(base_dir, "data/final", "Paytm_VOC_Authoritative_Final_Dataset.csv")
df = pd.read_csv(final_csv)
total_n = len(df)

# 1. Geography Visualizations
city_summary = df['City_Standardized'].value_counts().reset_index()
city_summary.columns = ['city', 'count']
city_summary['percentage'] = (city_summary['count'] / total_n * 100).round(2)
city_summary.to_json(os.path.join(base_dir, "visualizations/geography/city_distribution.json"), orient='records', indent=2)

state_summary = df['State_Standardized'].value_counts().reset_index()
state_summary.columns = ['state', 'count']
state_summary['percentage'] = (state_summary['count'] / total_n * 100).round(2)
state_summary.to_json(os.path.join(base_dir, "visualizations/geography/state_distribution.json"), orient='records', indent=2)

# 2. Demographics & Settlement
settle_summary = df['Settlement_Typology'].value_counts().reset_index()
settle_summary.columns = ['settlement', 'count']
settle_summary['percentage'] = (settle_summary['count'] / total_n * 100).round(2)
settle_summary.to_json(os.path.join(base_dir, "visualizations/demographics/settlement_distribution.json"), orient='records', indent=2)

# 3. Profession Distribution
prof_summary = df['1. Which best describes you?'].value_counts().reset_index()
prof_summary.columns = ['profession', 'count']
prof_summary['percentage'] = (prof_summary['count'] / total_n * 100).round(2)
prof_summary.to_json(os.path.join(base_dir, "visualizations/profession/profession_distribution.json"), orient='records', indent=2)

# 4. App Preference
app_summary = df['Primary_App_Clean'].value_counts().reset_index()
app_summary.columns = ['app', 'count']
app_summary['percentage'] = (app_summary['count'] / total_n * 100).round(2)
app_summary.to_json(os.path.join(base_dir, "visualizations/app_preference/primary_app_share.json"), orient='records', indent=2)

# 5. Copy Master Dashboard to visualizations/final/
shutil.copy2(os.path.join(base_dir, "index.html"), os.path.join(base_dir, "visualizations/final/master_dashboard.html"))
shutil.copy2(os.path.join(base_dir, "style.css"), os.path.join(base_dir, "visualizations/final/style.css"))
shutil.copy2(os.path.join(base_dir, "app.js"), os.path.join(base_dir, "visualizations/final/app.js"))
shutil.copy2(os.path.join(base_dir, "india_geo_data.js"), os.path.join(base_dir, "visualizations/final/india_geo_data.js"))

print("Populated all visualization directories and master dashboard.")
