import ollama
import json
from config import OLLAMA_URL

OLLAMA_ENDPOINT = f"{OLLAMA_URL}/api/generate"

client = ollama.Client()

model = "deepseek-r1"
prompt = """
    Generate just code in selenium python (no explanations or notes) based on this cucumber feature file, website used is saucedemo.com:
    Feature: User can add item to cart
    
        Scenario:
            Given I log in
            When I add a backpack to the cart
            Then the cart icon should show "1"
    """

response = client.generate(
    model=model, 
    prompt=prompt, 
    stream=True,
    think=False,
    # raw=True,
    options={
        # "num_predict": 100,
        "temperature": 0.2,
        # "stop": ["```"]
    }
    )

# print(response.response)
# print(json.dumps((response.response), indent=2))

for chunk in response:
    print(
        chunk.response, 
        end="", 
        flush=False
        )