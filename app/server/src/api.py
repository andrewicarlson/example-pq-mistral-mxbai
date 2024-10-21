import os
import psycopg
from ollama import Client
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pgvector.psycopg import register_vector
from dotenv import load_dotenv
from app.main import main

load_dotenv('./src/.env', override=True)

params = {
    'dbname': os.environ.get("POSTGRES_DB"),
    'user': os.environ.get("POSTGRES_USER"),
    'password': os.environ.get("POSTGRES_PASSWORD"),
    'host': os.environ.get("POSTGRES_HOST"),
    'port': os.environ.get("POSTGRES_PORT"),
    'autocommit': True
}

conn = psycopg.connect(**params)

conn.execute('CREATE EXTENSION IF NOT EXISTS vector')
register_vector(conn)

conn.execute('DROP TABLE IF EXISTS chatbot_demo')
conn.execute('CREATE TABLE chatbot_demo (id bigserial PRIMARY KEY, content text, embedding vector(1024), pq_id text, required_variables text)')

pq_details = [
    {
        'metadata': 'Information about all products. Title, description, price, and details about all products available for sale. query AllProducts { products { id name price stock description category } }',
        'pq_id': '1bb5e58db14e0aac786f4dc01c73063291955a570fffc7d1b6633371ae001286',
        'required_variables': {}
    },
    {
        'metadata': 'Information about a specific product. Can be queried by using a product name and will return information like the title, description, price, stock level, and details for a specific product. query Product($productName: String!) { product(product_name: $productName) { category description name id price stock } }',
        'pq_id': '40dcb3622e73833624726a85beec030a40da596c370f95adc9b84425445c6a42',
        'required_variables': {'productName': 'placeholder_text'}
    }
]

metadata = list(map(lambda el: el['metadata'], pq_details))

client = Client(host='http://host.docker.internal:11434')

response = client.embed(input=metadata, model=os.environ.get("EMBEDDINGS_MODEL_NAME"))

embeddings = [v for v in response["embeddings"]]

for content, embedding in zip(pq_details, embeddings):
    required_variables = f'{content.get("required_variables")}' or None
    conn.execute('INSERT INTO chatbot_demo (content, embedding, pq_id, required_variables) VALUES (%s, %s, %s, %s)', (content['metadata'], embedding, content['pq_id'], required_variables))

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root(question: str):
    return main(question=question, conn=conn)