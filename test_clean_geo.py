import pandas as pd
import json

df = pd.read_excel('Paytm UPI Growth Challenge 2026 — Raw Short VOC Responses.xlsx', sheet_name='Form Responses 1')

city_map = {
    'Sitapur ': 'Sitapur', 'Sitapur': 'Sitapur',
    'Bhopal': 'Bhopal', 'Bhopal ': 'Bhopal', 'bhopal': 'Bhopal', 'BHOPAL ': 'Bhopal',
    'Lucknow ': 'Lucknow', 'Lucknow': 'Lucknow',
    'Lakhimpur Kheri ': 'Lakhimpur Kheri', 'Kheri': 'Lakhimpur Kheri', 'Lakhimapur Kheri': 'Lakhimpur Kheri',
    'Shahjahanpur ': 'Shahjahanpur', 'Biswan': 'Biswan',
    'Ballia': 'Ballia', 'Vallia': 'Ballia',
    'Sehore': 'Sehore',
    'Bangalore': 'Bengaluru',
    'Hardoi': 'Hardoi', 'Hardoi ': 'Hardoi',
    'Delhi': 'Delhi (NCR)', 'Noida': 'Noida',
    'Gurgaon ': 'Gurgaon', 'gurugram ': 'Gurgaon',
    'Agra ': 'Agra', 'Agra': 'Agra',
    'Dehradun': 'Dehradun', 'Panipat': 'Panipat', 'Karnal ': 'Karnal',
    'Shimla': 'Shimla', 'Surat': 'Surat', 'Pune': 'Pune',
    'Sangali Maharashtra ': 'Sangli', 'Indore': 'Indore',
    'Bhubaneswar ': 'Bhubaneswar', 'Jamshedpur ': 'Jamshedpur',
    'Mathura': 'Mathura', 'Hamirpur ': 'Hamirpur', 'Prayagraj': 'Prayagraj',
    'Akbarpur ': 'Akbarpur', 'Laharpur': 'Laharpur', 'Babhnan ': 'Babhnan',
    'Kotwara po kotwara': 'Kotwara', 'Gaura ': 'Gaura',
    'Uttar Pradesh ': 'Uttar Pradesh (General)', 'Uttar Pradesh': 'Uttar Pradesh (General)',
    'Rajsthan': 'Rajasthan (General)', 'Riga , Latvia ': 'Overseas / Student'
}

df['city_std'] = df['2. Which city do you currently live in?'].map(city_map).fillna(df['2. Which city do you currently live in?'])

state_map = {
    'Sitapur': 'Uttar Pradesh', 'Lucknow': 'Uttar Pradesh', 'Lakhimpur Kheri': 'Uttar Pradesh',
    'Shahjahanpur': 'Uttar Pradesh', 'Biswan': 'Uttar Pradesh', 'Hardoi': 'Uttar Pradesh',
    'Ballia': 'Uttar Pradesh', 'Agra': 'Uttar Pradesh', 'Noida': 'Uttar Pradesh',
    'Mathura': 'Uttar Pradesh', 'Hamirpur': 'Uttar Pradesh', 'Prayagraj': 'Uttar Pradesh',
    'Akbarpur': 'Uttar Pradesh', 'Laharpur': 'Uttar Pradesh', 'Babhnan': 'Uttar Pradesh',
    'Kotwara': 'Uttar Pradesh', 'Gaura': 'Uttar Pradesh', 'Uttar Pradesh (General)': 'Uttar Pradesh',
    'Bhopal': 'Madhya Pradesh', 'Sehore': 'Madhya Pradesh', 'Indore': 'Madhya Pradesh',
    'Delhi (NCR)': 'Delhi (NCR)', 'Gurgaon': 'Haryana', 'Panipat': 'Haryana', 'Karnal': 'Haryana',
    'Bengaluru': 'Karnataka', 'Pune': 'Maharashtra', 'Sangli': 'Maharashtra', 'Surat': 'Gujarat',
    'Dehradun': 'Uttarakhand', 'Shimla': 'Himachal Pradesh', 'Bhubaneswar': 'Odisha',
    'Jamshedpur': 'Jharkhand', 'Rajasthan (General)': 'Rajasthan', 'Overseas / Student': 'Other'
}
df['state_std'] = df['city_std'].map(state_map).fillna('Other')

city_coords = {
    'Sitapur': [80.6780, 27.5684],
    'Bhopal': [77.4126, 23.2599],
    'Lucknow': [80.9462, 26.8467],
    'Lakhimpur Kheri': [80.7777, 27.9458],
    'Ballia': [84.1497, 25.7581],
    'Shahjahanpur': [79.9122, 27.8805],
    'Biswan': [81.0028, 27.4939],
    'Hardoi': [80.1264, 27.3989],
    'Sehore': [77.0847, 23.2032],
    'Gurgaon': [77.0266, 28.4595],
    'Bengaluru': [77.5946, 12.9716],
    'Agra': [78.0081, 27.1767],
    'Delhi (NCR)': [77.1025, 28.7041],
    'Noida': [77.3910, 28.5355],
    'Dehradun': [78.0322, 30.3165],
    'Panipat': [76.9635, 29.3909],
    'Karnal': [76.9897, 29.6857],
    'Shimla': [77.1734, 31.1048],
    'Surat': [72.8311, 21.1702],
    'Pune': [73.8567, 18.5204],
    'Sangli': [74.5815, 16.8524],
    'Indore': [75.8577, 22.7196],
    'Bhubaneswar': [85.8245, 20.2961],
    'Jamshedpur': [86.2029, 22.8046],
    'Mathura': [77.6737, 27.4924],
    'Hamirpur': [80.1517, 25.9554],
    'Prayagraj': [81.8463, 25.4358],
    'Akbarpur': [82.5369, 26.4351],
    'Laharpur': [80.9042, 27.7167],
    'Babhnan': [82.3850, 26.9600],
    'Kotwara': [81.2000, 27.1000],
    'Gaura': [81.6000, 26.1000]
}

city_counts = df['city_std'].value_counts()
state_counts = df['state_std'].value_counts()

print("Real State Counts:\n", state_counts)
print("\nReal City Counts (Top 15):\n", city_counts.head(15))
