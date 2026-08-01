import os
import requests
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}"
}

response = requests.get(
    "https://openrouter.ai/api/v1/models",
    headers=headers,
)

models = response.json()["data"]

print("\nFREE MODELS:\n")

for model in models:
    if model.get("pricing", {}).get("prompt") == "0":
        print(model["id"])