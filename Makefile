IMAGE_NAME = flask_todo
APP_PORT = 8000

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run -p $(APP_PORT):$(APP_PORT) $(IMAGE_NAME)

# Clean up Docker resources (containers and images)
clean:
	docker stop $$(docker ps -a -q)
	docker rm $$(docker ps -a -q)
	docker rmi $(IMAGE_NAME)


