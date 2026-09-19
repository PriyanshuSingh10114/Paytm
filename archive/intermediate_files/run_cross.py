import subprocess

with open('cross_analysis_output.txt', 'w', encoding='utf-8') as f:
    subprocess.run(['python', 'cross_analysis.py'], stdout=f, stderr=subprocess.STDOUT)

print("Saved cross_analysis_output.txt")
