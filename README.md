# docker-image-for-Yelp-dataset-analytics
These are the the files used to create the Yelp-dataset-analytics docker image found here:
https://hub.docker.com/r/omar1456/customer-analytics [![Docker Pulls](https://img.shields.io/docker/pulls/omar1456/customer-analytics?style=flat-square)](https://hub.docker.com/r/omar1456/customer-analytics)

## dataset
The dataset included in the image is a **sample of the Yelp dataset** found here:  
https://www.kaggle.com/datasets/luisfredgs/yelp-reviews-csv?select=yelp_review.csv  

You can download the **full dataset** and rebuild the Docker image locally using the provided commands, avoiding the need to include the full dataset in the image.  

The full dataset has a shape of **(5,261,668, 9)** and the following columns:  
`[review_id, user_id, business_id, stars, date, text, useful, funny, cool]`

## pipeline

The project implements a full data processing pipeline inside Docker.  
Each script calls the next one and passes the processed dataset as input.

Pipeline flow:

ingest.py → preprocess.py → analytics.py → visualize.py → cluster.py

Each one calls the next one 
After that manually call the summary script 

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

- **summary.sh**
  - Copies all output files from container to `results/`
  -Stops and removes the container

---

## how it runs

### 1. Build Docker image

```bash
docker build -t customer-analytics 
```
### 2. Run container
```bash
docker run -it --name customer-container customer-analytics
```
### 3. Run pipeline inside container
```bash
python ingest.py yelp_review.csv
```
This will automatically execute the full pipeline.

### 4. Exit container
```bash
exit
```
### 5. Copy results to local machine and clean up
On Windows PowerShell:
```bash
.\summary.ps1
```
or

On Git Bash:
```bash
./summary.sh
```
## other files
- **eda.ipynb**
  - Simple EDA notebook used to:
  - Generate a smaller sample dataset used for testing and building the Docker image

- **dockerfile**
  - Used to create the image

- **.dockerignore**
  - Used to ignore unnecessary files when building the Docker image

- **summary.sh**
  - Bash script used in Git Bash
  - Copies all output files from container to results/
  - Stops and removes the container

- **summary.ps1**
  - PowerShell version of summary.sh
