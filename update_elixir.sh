#!/bin/bash

# Define variables
CONTAINER_NAME="elixir-v3"
IMAGE_NAME="elixirprotocol/validator:v3"
ENV_FILE="/path/to/validator.env"
PORT_MAPPING="17690:17690"
PLATFORM="linux/amd64"

# Stop and remove the existing container if it exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping and removing the existing container: $CONTAINER_NAME..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
else
    echo "No existing container to stop or remove."
fi

# Pull the latest image
echo "Pulling the latest image: $IMAGE_NAME..."
docker pull --platform $PLATFORM $IMAGE_NAME

# Run the new container
echo "Running a new container: $CONTAINER_NAME..."
docker run -d \
    --env-file $ENV_FILE \
    --platform $PLATFORM \
    -p $PORT_MAPPING \
    --name $CONTAINER_NAME \
    --restart unless-stopped \
    $IMAGE_NAME

echo "Container $CONTAINER_NAME is up and running!"