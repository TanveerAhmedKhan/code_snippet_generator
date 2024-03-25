# Code Snippet Generator

## Overview
This project provides a web-based interface for generating code snippets using OpenAI's GPT model. The backend is built with FastAPI and interacts with OpenAI's API to generate code based on user requests. The frontend provides a simple chat interface for users to submit their code generation queries.

## Features
- Web interface for submitting code generation requests.
- Backend service using FastAPI and OpenAI for processing and responding to user queries.
- Cross-Origin Resource Sharing (CORS) enabled for broad compatibility.
- Dockerized application for easy deployment and scalability.

## Installation

### Prerequisites
- Docker and Docker Compose
- Python 3.8 or later

### Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the root directory of the project.
3. Ensure you have a `.env` file in the /src directory with your OpenAI API key and organization key:
openai_key="<your_openai_api_key>"
org_key="<your_openai_organization_key>"

4. Build the Docker images and start the services using Docker Compose:

```bash
docker-compose up --build
```


## Running the Project
Once the Docker containers are up and running, you can access the services as follows:

## Backend (FastAPI):
The backend service is available at http://localhost:8000. You can access the FastAPI documentation and test the API directly by navigating to http://localhost:8000/docs.

## Frontend: 
The frontend can be accessed at http://localhost:5500. Here you can interact with the chat interface to send code generation requests and receive responses.

## Usage
To generate a code snippet, follow these steps:

1. Go to http://localhost:5500 in your web browser.
2. In the chat interface, type your code generation request in the message input box.
3. Press Enter or click the Send button to submit your request.
4. The generated code snippet will be displayed in the chat interface.

## Contributing
Feel free to fork the project and submit pull requests with enhancements or fixes. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT

## Contact
For any questions or suggestions, please reach out to [Your Contact Information].