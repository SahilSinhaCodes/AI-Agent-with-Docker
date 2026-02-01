import os
from langchain_openai import ChatOpenAI

# 1. Set the default to the Smart 70B model (Safety Net)
OPENAI_MODEL_NAME = os.environ.get('OPENAI_MODEL_NAME') or 'llama-3.3-70b-versatile'
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL = os.environ.get('OPENAI_BASE_URL')

if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY is missing!")

def get_openai_llm():
    openai_params = {
        "model": OPENAI_MODEL_NAME,
        "api_key": OPENAI_API_KEY,
        # 2. CRITICAL FIX: Set temperature to 0.
        # This stops the model from hallucinating weird brackets like []
        "temperature": 0
    }

    if OPENAI_BASE_URL:
        openai_params['base_url'] = OPENAI_BASE_URL

    return ChatOpenAI(**openai_params)