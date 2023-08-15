# Flask Todo App

Welcome to the Flask Todo App repository!

## Project Setup

Follow these instructions to set up the project on your local machine.

1. **Clone the Repository:** Begin by cloning this repository to your preferred location on your machine:

   ```bash
   git clone https://github.com/huzaifakhan771/flask_todo.git

2. **Navigate to the Project Directory:** Move into the project directory:
    ```bash
    cd flask_todo

3. **Build the Docker Image:** Build the Docker image for the Flask Todo App by running the following command:
   ```bash
    make build

4. **Run the Docker Container:** Once the image is built, start the Docker container with the following command:
   ```bash
    make run

5. **Access the App:** You can now access the Flask Todo App by visiting and navigating to http://localhost:8000/api/ui or
any API platform like [Postman](https://www.postman.com/).

6. **Create a User:**
   Go to ```http://localhost:8000/api/auth/register``` for create a user, and ```http://localhost:8000/api/auth/login``` to create
   an API token to access the endpoints.

6. **Clean Up Docker Resources [Optional]:** When you're done using the app, you can clean up the Docker resources (stop containers and remove the image) using:
   ```bash
   make clean
