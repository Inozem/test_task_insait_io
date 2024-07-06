# Flask OpenAI Question Answering Service

## Introduction
This project is a simple Flask application that exposes an endpoint to ask a question. The server sends the question to the OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database. The server and the database are dockerized and run with Docker Compose. Tests are implemented using pytest.

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
    docker-compose up --build
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
