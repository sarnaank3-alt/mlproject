#!/bin/bash

# Navigate to the Terraform directory
cd infra/terraform

# Initialize Terraform
terraform init

# Apply the Terraform configuration
terraform apply -auto-approve

# Build Docker images for the backend and Streamlit UI
docker build -t entertainment-supplychain-genai-chatbot-backend ../app/backend
docker build -t entertainment-supplychain-genai-chatbot-streamlit ../app/streamlit_ui

# Push Docker images to ECR (Elastic Container Registry)
# Assuming ECR login has been done previously
docker tag entertainment-supplychain-genai-chatbot-backend:latest <your_ecr_repo>/entertainment-supplychain-genai-chatbot-backend:latest
docker tag entertainment-supplychain-genai-chatbot-streamlit:latest <your_ecr_repo>/entertainment-supplychain-genai-chatbot-streamlit:latest

docker push <your_ecr_repo>/entertainment-supplychain-genai-chatbot-backend:latest
docker push <your_ecr_repo>/entertainment-supplychain-genai-chatbot-streamlit:latest

# Clean up local Docker images
docker rmi entertainment-supplychain-genai-chatbot-backend:latest
docker rmi entertainment-supplychain-genai-chatbot-streamlit:latest

echo "Deployment completed successfully."