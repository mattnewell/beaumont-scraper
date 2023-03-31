# Variables
REGION = us-east-2
ACCOUNT_ID = 566613373177
ECR_REPO = scraper
IMAGE_TAG = latest

# Build, tag, and push the Docker image to ECR
build_and_push: docker_build docker_tag ecr_login docker_push

# Build the Docker image
docker_build:
	@echo "Building Docker image..."
	docker build -t $(ECR_REPO):$(IMAGE_TAG) .

# Tag the Docker image with the ECR repository URL
docker_tag:
	@echo "Tagging Docker image..."
	docker tag $(ECR_REPO):$(IMAGE_TAG) $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com/$(ECR_REPO):$(IMAGE_TAG)

# Log in to ECR
ecr_login:
	@echo "Logging in to ECR..."
	aws ecr get-login-password --region $(REGION) | docker login --username AWS --password-stdin $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com

# Push the Docker image to ECR
docker_push:
	@echo "Pushing Docker image to ECR..."
	docker push $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com/$(ECR_REPO):$(IMAGE_TAG)

.PHONY: build_and_push docker_build docker_tag ecr_login docker_push
