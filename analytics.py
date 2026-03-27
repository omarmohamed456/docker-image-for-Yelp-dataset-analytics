import pandas as pd
import sys
import subprocess

print("analytics.py called successfully")

# Get CSV input path from command line
if len(sys.argv) < 2:
    print("Usage: python analytics.py <preprocessed_csv>")
    sys.exit(1)

input_csv = sys.argv[1]

#Load preprocessed dataset
df = pd.read_csv(input_csv)

#Insight 1: Average review length by stars_binned

avg_length = df.groupby('stars_binned')['review_length'].mean()
insight1 = "Average review length by star category:\n"
for category, length in avg_length.items():
    insight1 += f"{category}: {length:.2f} characters\n"

#Save
with open("insight1.txt", "w") as f:
    f.write(insight1)

print("Saved insight1.txt")

#Insight 2: Average usefulness, funny, and cool counts by stars_binned

avg_metrics = df.groupby('stars_binned')[['useful', 'funny', 'cool']].mean()
insight2 = "Average engagement metrics by star category:\n"
for category, row in avg_metrics.iterrows():
    insight2 += f"{category}: useful={row['useful']:.2f}, funny={row['funny']:.2f}, cool={row['cool']:.2f}\n"

#Save 
with open("insight2.txt", "w") as f:
    f.write(insight2)

print("Saved insight2.txt")

#Insight 3: Distribution of stars_binned

distribution = df['stars_binned'].value_counts(normalize=True) * 100
insight3 = "Distribution of reviews by star category (%):\n"
for category, pct in distribution.items():
    insight3 += f"{category}: {pct:.2f}%\n"

#Save 
with open("insight3.txt", "w") as f:
    f.write(insight3)

print("Saved insight3.txt")

#call visualize..py
subprocess.run(["python", "visualize.py", input_csv])