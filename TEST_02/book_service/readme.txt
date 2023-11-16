## Step 1: Install Docker and Docker Compose
Follow the official Docker documentation for installation:

- Docker Installation
- Docker Compose Installation

##Step 2: Set Up Project Directory
Create a new directory for the project and navigate to it in the terminal.

##Step 3: Create Project Files
Inside the project directory, create the necessary project files as described in the initial project structure:

app/__init__.py
app/main.py
app/models.py
app/database.py
Dockerfile
docker-compose.yml

##Build and Run Docker Containers
Open a terminal in the project directory and run the following command to build and run the Docker containers:

>> docker-compose up --build

This command will build the Docker images, create containers, and start the FastAPI application and PostgreSQL database.


## Step 5: Secure the API (Optional)
If  implemented token-based authentication.

## Step 7: Stop and Clean Up
When done testing the application, you can stop the containers by pressing 'Ctrl + C' in the terminal where the containers are running.