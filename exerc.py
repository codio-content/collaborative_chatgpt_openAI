import os
import openai
import secret

openai.api_key=secret.api_key
# CODIO SOLUTION BEGIN
def collaborative_chat_gpt(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a knowledgeable assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# CODIO SOLUTION END

