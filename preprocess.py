import pandas as pd
import sys

#Load dataset

if len(sys.argv) < 2:
    print("Usage: python preprocess.py <input_csv>")
    sys.exit(1)

input_csv = sys.argv[1]


df = pd.read_csv(input_csv)

#Data Cleaning

# Missing values
missing_count = df.isnull().sum().sum()
if missing_count == 0:
    print("No missing values found.")
else:
    missing_cols = df.columns[df.isnull().any()].tolist()
    df = df.dropna()
    print(f"Dropped rows with missing values in columns: {missing_cols}")
# Duplicates
duplicate_count = df.duplicated().sum()
if duplicate_count == 0:
    print("No duplicates found.")
else:
    df = df.drop_duplicates(keep='first')
    print(f"Dropped {duplicate_count} duplicate rows.")

#Feature Transformation
df['review_length'] = df['text'].apply(lambda x: len(str(x)))
print("Added column: 'review_length'")

#Dimensionality Reduction
columns_to_keep = ['stars','date', 'useful', 'funny', 'cool', 'review_length']
dropped_cols = [col for col in df.columns if col not in columns_to_keep]
df = df[columns_to_keep]
print(f"Dropped the following columns for dimensionality reduction: {dropped_cols}")

#Discretization

def stars_bin(star):
    if star <= 2:
        return 'low'
    elif star == 3 or star == 4:
        return 'medium'
    else:
        return 'high'

df['stars_binned'] = df['stars'].apply(stars_bin)
print("Added column: 'stars_binned'")

#Save preprocessed data
df.to_csv("data_preprocessed.csv", index=False)
print("Preprocessed data Saved to data_preprocessed.csv")