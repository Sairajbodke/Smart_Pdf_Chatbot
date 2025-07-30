import openai

openai.api_key = "API KEY"
openai.api_base = "https://api.together.xyz/v1"

def get_together_response(context, question):
    prompt = f"""
You are a helpful assistant. Use the following context to answer the user's question.

Context:
{context}

Question: {question}
Answer:
"""
    response = openai.ChatCompletion.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
