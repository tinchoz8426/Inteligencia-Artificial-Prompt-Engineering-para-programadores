import requests # pip install requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer API_KEY_OPENROUTER",
        "Content-Type": "application/json",
    },
    data=json.dumps(
        {
            "model": "deepseek/deepseek-r1-distill-llama-70b:free",
            "messages": [{"role": "user", "content": "¿Que es un algoritmo de búsqueda binaria?"}],
        }
    ),
)

print(response.json()["choices"][0]["message"]["content"])