# Container name
$container = "customer-container"

# Create results folder if not exists
New-Item -ItemType Directory -Force -Path results

# Copy files from container to host (note string concatenation with +)
docker cp ($container + ":/app/pipeline/data_raw.csv") results/
docker cp ($container + ":/app/pipeline/data_preprocessed.csv") results/
docker cp ($container + ":/app/pipeline/insight1.txt") results/
docker cp ($container + ":/app/pipeline/insight2.txt") results/
docker cp ($container + ":/app/pipeline/insight3.txt") results/
docker cp ($container + ":/app/pipeline/summary_plot.png") results/
docker cp ($container + ":/app/pipeline/clusters.txt") results/

Write-Output "Files copied to results/"

# Stop container
docker stop $container

# Remove container
docker rm $container

Write-Output "Container stopped and removed"