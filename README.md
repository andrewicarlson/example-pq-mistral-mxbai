# Safe and trusted API access with Chatbots and GraphQL

This repository demonstrates how to execute safe and trusted operations in an API from an LLM-driven chatbot. It leverages functionality from Apollo GraphOS such as [Persisted Queries](https://www.apollographql.com/docs/router/configuration/persisted-queries/#differences-from-automatic-persisted-queries) and [Contracts](https://www.apollographql.com/docs/graphos/delivery/contracts/).

## Running the Example

### Apollo Enterprise Trial

1. Start an [Enterprise Trial](https://studio.apollographql.com/signup?type=enterprise-trial_) for the persisted queries
1. In [Apollo Studio](https://studio.apollographql.com/) create a new graph and ensure that 'Supergraph' is selected for 'Graph Architecture'.
1. In the next overlay screen, copy the `APOLLO_KEY` and the Graph reference. It should look something like `My-Graph-5-2jlmak@current`
1. Create `/router/.env` based on `/router/.env.example` which exports the `APOLLO_KEY` and `APOLLO_GRAPH_REF` previously copied.

### Set up

1. Create a new `.env` file using the format from `/app/server/src/.env.example` and change the details of the PGVector instance if necessary. The details provided will work with the PGVector container included in this demo.
1. Download [Ollama](https://ollama.com/download) and [Docker](https://www.docker.com/products/docker-desktop/)
1. Pull local models and start the model server using `sh scripts/ollama.sh`
1. From the project root run `docker-compose up` to create the containers for the vector database, python server which interacts with the local LLM and embedding models, client application, subgraph server, and router.
1. Once the Docker containers are all running, visit `http://localhost:3000` in a browser. You should see a rudimentary chat box. You can ask simple questions like: "What products do you sell" and "How much does a papaya cost" and it will find the correct Persisted Query and issue it to the router. Note: Results vary _widely_ based on the LLM model that is used. ChatGPT 4o works much differently than Mistral, so some prompt tuning will be required. 
