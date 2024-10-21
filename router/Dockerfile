FROM debian:bullseye-slim
RUN apt-get update && apt-get install -y \
curl
WORKDIR /app
COPY create_local_schema.sh start_router.sh download_router.sh download_rover.sh persistedQueryManifest.json router-config.yaml supergraph.yaml .env ./
RUN sh download_router.sh && sh download_rover.sh
CMD sh create_local_schema.sh && sh start_router.sh