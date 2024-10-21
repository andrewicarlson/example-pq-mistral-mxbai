#!/bin/bash
source .env

APOLLO_KEY=$APOLLO_KEY APOLLO_GRAPH_REF=$APOLLO_GRAPH_REF ./router \
  --dev \
  --config router-config.yaml \
  --supergraph schema.graphql