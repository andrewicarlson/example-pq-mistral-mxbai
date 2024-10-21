import os
import sys
import psycopg
import json
from ollama import Client

from dotenv import load_dotenv
from pgvector.psycopg import register_vector
import requests

load_dotenv('./src/.env', override=True)

def main(question: str, conn):
    client = Client(host='http://host.docker.internal:11434')
    query_embedding = client.embed(input=question, model=os.environ.get("EMBEDDINGS_MODEL_NAME"))

    neighbors = conn.execute('SELECT id,content,pq_id,required_variables FROM chatbot_demo ORDER BY embedding <-> (%s) LIMIT 3', [f'{query_embedding["embeddings"][0]}']).fetchall()
    
    formatted_vector_response = list(map(lambda el: {"id": el[0], "content": el[1], "pq_id": el[2], "required_variables": el[3]}, neighbors))

    post_processing_prompt = """In your response, only return a JSON object using the following rules:
    1. The format must be { pq_id: PQ_ID_HERE, required_variables: REQUIRED_VARIABLES_HERE }
    2. Replace 'PQ_ID_HERE' with the value from the selected JSON object. 
    3. If the selected JSON object contains a 'required_variables' property, replace all text labeled 'placeholder_text' with the most applicable term from the user question. For example, if a required variable is 'category' replace 'placeholder_text' with a category specified by the user.
    4. Under no circumstances return anything other than the JSON object. Do not wrap it in any other string, backticks, or characters."""

    most_valid_neighbor = client.generate(
        model=os.environ.get("CHAT_MODEL_NAME"),
        prompt=f"""
                ${question}

                Which of the corresponding `pq_id`s from the following JSON object would best satisfy the previous request? ${formatted_vector_response}.
                
                ${post_processing_prompt}
                """
    )

    pq_json = json.loads(most_valid_neighbor["response"])

    if (pq_json.get("pq_id")) :
        request = requests.post(
            'http://host.docker.internal:4040', 
            headers={
                'content-type': 'application/json',
            },
            data=json.dumps({
                'extensions': {
                    'persistedQuery': {
                        'version': 1,
                        'sha256Hash': pq_json["pq_id"]
                    }
                },
                'variables': pq_json.get("required_variables", {})
            })
        )

        chat_response = client.generate(
            model=os.environ.get("CHAT_MODEL_NAME"),
            prompt=f"""
                    ${question}

                    Summarize the following JSON body into up to 3 human readable sentences as an answer to the previous question: {request.json()}
                    """
        )

        return chat_response["response"]

    return "Sorry, I can't answer questions about that. Try asking about our products."