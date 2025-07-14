import requests
import json

from config import OLLAMA_URL

OLLAMA_ENDPOINT = f"{OLLAMA_URL}/api/chat"

payload = {
    "model": "deepseek-r1",
    "messages": [
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
}

response = requests.post(OLLAMA_ENDPOINT, json=payload, stream=True)

if response.ok:
    print("Streaming res from Ollama")
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                data = json.loads(line)
                print(data["message"]["content"], end="")
            except json.JSONDecodeError:
                print("Error decoding JSON:", line)
    print()
else:
    print(f"Error: {response.status_code} - {response.text}")