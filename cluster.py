# cluster.py

import pandas as pd
import sys
from sklearn.cluster import KMeans

print("cluster.py called successfully")

#Get CSV input path
if len(sys.argv) < 2:
    print("Usage: python cluster.py <preprocessed_csv>")
    sys.exit(1)

input_csv = sys.argv[1]

#Load dataset
df = pd.read_csv(input_csv)

#Select features for clustering
features = ['stars', 'review_length', 'useful', 'funny', 'cool']
X = df[features]

print(f"Using features for clustering: {features}")

#Apply K-Means
k = 3  
kmeans = KMeans(n_clusters=k, random_state=42)

df['cluster'] = kmeans.fit_predict(X)

print("K-Means clustering applied.")

#Count samples per cluster
cluster_counts = df['cluster'].value_counts().sort_index()

#Save results
with open("clusters.txt", "w") as f:
    for cluster_id, count in cluster_counts.items():
        f.write(f"Cluster {cluster_id}: {count} samples\n")

print("Saved clusters.txt")