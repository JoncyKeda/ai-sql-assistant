import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_sql(user_query, schema):
    prompt = f"""
    You are an expert SQL generator.

    Database schema:
    {schema}

    Convert the following natural language query into SQL.
    Only return SQL query, no explanation.

    Query:
    {user_query}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
