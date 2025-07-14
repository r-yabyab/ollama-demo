import ollama
import json
from config import OLLAMA_URL

OLLAMA_ENDPOINT = f"{OLLAMA_URL}/api/generate"

client = ollama.Client()

model = "deepseek-r1"
prompt = "Hello world!"

response = client.generate(
    model=model, 
    prompt=prompt, 
    stream=True
    )

# print(response.response)
# print(json.dumps((response.response), indent=2))

for chunk in response:
    # Print each partial response string as it comes, without newline
    print(chunk.response, end="", flush=False)