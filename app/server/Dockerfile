FROM python:3.12.2
WORKDIR /app
COPY src startup requirements.txt ./
RUN pip install -r requirements.txt
CMD fastapi dev /app/src/api.py --host 0.0.0.0
