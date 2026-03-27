import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess

print("visualize.py called successfully")


#Get CSV input path

if len(sys.argv) < 2:
    print("Usage: python visualize.py <preprocessed_csv>")
    sys.exit(1)

input_csv = sys.argv[1]

#Load dataset
df = pd.read_csv(input_csv)

#fixed size
plt.figure(figsize=(18, 5))

#Histogram of stars
plt.subplot(1, 3, 1)
plt.hist(df['stars'], bins=5)
plt.title("Histogram of Stars")
plt.xlabel("Stars")
plt.ylabel("Count")

#Review length distribution
plt.subplot(1, 3, 2)
plt.hist(df['review_length'], bins=30)
plt.title("Review Length Distribution")
plt.xlabel("Review Length")
plt.ylabel("Count")

#Correlation heatmap
plt.subplot(1, 3, 3)
corr = df[['stars', 'useful', 'funny', 'cool', 'review_length']].corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")

#Save plot
plt.tight_layout()
plt.savefig("summary_plot.png")
plt.close()

print("Saved summary_plot.png")

#Call cluster.py
subprocess.run(["python", "cluster.py", input_csv])