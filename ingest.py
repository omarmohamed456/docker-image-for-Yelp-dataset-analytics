import sys
import pandas as pd
import subprocess

def main():
    print("loading dataset")
    
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <dataset_path>")
        sys.exit(1)

    input_path = sys.argv[1]

    # Load dataset
    df = pd.read_csv(input_path)

    # Save raw copy
    output_path = "data_raw.csv"
    df.to_csv(output_path, index=False)

    print(f"Raw data saved to {output_path}")

    # Call next script
    subprocess.run(["python", "preprocess.py", output_path])

if __name__ == "__main__":
    main()