# Flask OpenAI Question Answering Service

## Introduction
This project was created as a home assignment for the Senior Backend Developer position at INSAIT. The task involves setting up a Flask server that exposes an endpoint to ask a question, integrates with the OpenAI API to get answers, and stores the questions and answers in a PostgreSQL database. The server and the database are dockerized and run with Docker Compose. Tests are implemented using pytest.

## Home Assignment Task Overview
Create a simple Flask server that exposes an endpoint to ask a question. The server sends the question to an OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database. The server and the database should be dockerized and run with Docker Compose. Implement one test using pytest.

### Requirements
1. Flask Server: Set up a Flask server with an endpoint to handle questions.
2. OpenAI API Integration: Integrate the OpenAI API to get answers for the questions.
3. Database: Use PostgreSQL to store questions and answers.
4. Alembic: Use Alembic for database migrations.
5. Docker: Dockerize the Flask server and the PostgreSQL database.
6. Docker Compose: Use Docker Compose to manage and run the containers.
7. Testing: Implement at least one test using pytest.
8. GitHub Repository: Share the code via a GitHub repository with a clean structure and meaningful commit history.
9. Best Practices for DAL: Implement best practices for Data Access Layer.

### Instructions
1. Flask Server:
   - Create a Flask application.
   - Create an endpoint `/ask` that accepts a POST request with a JSON payload containing the question.
2. OpenAI API:
   - Use the OpenAI API to get an answer for the question.
   - You can use the OpenAI Python client library for this. (You can create an account and use the free tier)
3. Database:
   - Set up a PostgreSQL database.
   - Create the schema.
   - Use SQLAlchemy for ORM. (or any other ORM)
   - Use Alembic for database migrations. (or any other migration tool)
4. Dockerization:
   - Dockerize the Flask application.
   - Dockerize the PostgreSQL database.
   - Use Docker Compose to run both containers.
5. Testing:
   - Implement one test using pytest to ensure the endpoint works as expected.
6. GitHub Repository:
   - Maintain a clean directory structure.
   - Ensure meaningful commit messages.
   - Use branches if necessary and document your work in the README file.

## Requirements
- Docker 
- Docker Compose
- Python 3.9
- OpenAI API Key

## Installation
1. Clone the repository:
    ```sh
    git clone git@github.com:Inozem/test_task_insait_io.git
    cd test_task_insait_io/application
    ```

2. Create an `.env` file with the following content in the "application" folder:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

3. Build and run the containers:
    ```sh
    docker-compose up -d --build
    ```

4. Apply the migrations:
    ```sh
    docker-compose run web alembic upgrade head
    ```

## Usage
1. Send a POST request to the `/ask` endpoint with a JSON payload containing the question:
    ```sh
    curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"question": "What is the capital of France?"}'
    ```

2. The server will respond with the question and the answer and save both in the database.

## Testing
1. Run the tests using pytest:
    ```sh
    pytest .\application\tests
    ```
