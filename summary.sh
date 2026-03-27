#!/bin/bash

# Container name
CONTAINER_NAME=customer-container

# Create results folder if not exists
mkdir -p results

# Copy files from container to host
docker cp $CONTAINER_NAME:/app/pipeline/data_raw.csv results/
docker cp $CONTAINER_NAME:/app/pipeline/data_preprocessed.csv results/
docker cp $CONTAINER_NAME:/app/pipeline/insight1.txt results/
docker cp $CONTAINER_NAME:/app/pipeline/insight2.txt results/
docker cp $CONTAINER_NAME:/app/pipeline/insight3.txt results/
docker cp $CONTAINER_NAME:/app/pipeline/summary_plot.png results/
docker cp $CONTAINER_NAME:/app/pipeline/clusters.txt results/

echo "Files copied to results/"

# Stop container
docker stop $CONTAINER_NAME

# Remove container
docker rm $CONTAINER_NAME

echo "Container stopped and removed"