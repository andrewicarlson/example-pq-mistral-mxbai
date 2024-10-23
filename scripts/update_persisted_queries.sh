#!/bin/bash
source ./router/.env

rover persisted-queries publish $APOLLOL_GRAPH_REF --manifest ./router/persistedQueryManifest.json