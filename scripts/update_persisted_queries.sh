#!/bin/bash
source ./router/.env

rover persisted-queries publish $APOLLO_GRAPH_REF --manifest ./router/persistedQueryManifest.json