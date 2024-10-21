# Set up

1. Download [Ollama](https://ollama.com/download) and [Docker](https://www.docker.com/products/docker-desktop/)
2. Run `docker-compose up` to create the containers for the vector database and python server which interacts with the local LLM and embedding models.
3. Run `sh ./scripts/ollama.sh` to start the Ollama service for access to local models.