# Vertex AI API
A microservice that provides a REST API for Vertex AI. This microservice is built using Flask and deployed on Google Cloud Run.

Access the API at: https://vertexai-api-ar2ndw3szq-uc.a.run.app

## Tech used:
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Google Cloud Run]()
- [Google Cloud Build](https://cloud.google.com/build)
- [Docker](https://www.docker.com/)
- [Vertex AI](https://cloud.google.com/vertex-ai)
- [Gooogle Translate](https://cloud.google.com/translate)

## Features
- Text Translation
- Text to Speech
- Medical Query
- Mental Health Query

## Installation

1. - Fork the [repo](https://gitlab.niveussolutions.com/niv-hack/niv-hack-2023/t3-tribe/vertexai-api)
   - Clone the repo to your local system
   ```git
   git clone https://gitlab.niveussolutions.com/niv-hack/niv-hack-2023/t3-tribe/vertexai-api.git
   cd vertexai-api
   ```

2. Create a virtual environment and activate it
   ```bash:
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the dependencies
    ```bash:
    pip3 install -r requirements.txt
    ```

4. Generate a Google Service Account config file and save it in a file named CREDENTIALS in env.

5. Then, run the development server:
    ```bash:
    python3 main.py
    ```

## Installation using Docker
1. Build the Docker image using the following command:
    ```bash:
    docker build -t vertexai-api .
    ```

2. Run the Docker container using the following command:
    ```bash:
    docker run -p 80:80 -e .env vertexai-api
    ```


