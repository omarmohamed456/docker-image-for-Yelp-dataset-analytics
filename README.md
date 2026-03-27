# docker-image-for-Yelp-dataset-analytics
These are the the files used to create the Yelp-dataset-analytics docker image

## dataset
dataset used is the Yelp dataset found here 
https://www.kaggle.com/datasets/luisfredgs/yelp-reviews-csv?select=yelp_review.csv
The datset shape is (5261668, 9)
Coulumns are [review_id, user_id, business_id, stars, date, text, useful, funny, cool]

## pipeline

The project implements a full data processing pipeline inside Docker.  
Each script calls the next one and passes the processed dataset as input.

Pipeline flow:

ingest.py → preprocess.py → analytics.py → visualize.py → cluster.py

### Stages

- **Ingestion**
  - Loads the dataset
  - Creates a smaller sample for processing
  - Saves as `data_raw.csv`

- **Preprocessing**
  - Handles missing values and duplicates
  - Creates `review_length` feature
  - Selects relevant columns
  - Discretizes `stars` into categories (low/medium/high)
  - Saves as `data_preprocessed.csv`

- **Analytics**
  - Generates textual insights
  - Saves them into:
    - `insight1.txt`
    - `insight2.txt`
    - `insight3.txt`

- **Visualization**
  - Creates:
    - Histogram of stars
    - Histogram of review length
    - Correlation heatmap
  - Saves as `summary_plot.png`

- **Clustering**
  - Applies K-Means clustering
  - Outputs number of samples per cluster
  - Saves as `clusters.txt`

---

## how it runs

### 1. Build Docker image

```bash
docker build -t customer-analytics 