#!/bin/bash
source .env

APOLLO_KEY=$APOLLO_KEY /root/.rover/bin/rover supergraph compose --config supergraph.yaml --output schema.graphql