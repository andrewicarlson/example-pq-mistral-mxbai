#!/bin/bash
docker exec -it chatbot_demo_app fastapi dev /app/src/api.py --host 0.0.0.0
