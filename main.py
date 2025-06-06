from services.llm_provider import LLM_PROVIDER
from fastapi import FastAPI
import json

# constants
data = FastAPI()

@data.post('/webhook')
def webhook():
    data = json.loads()
    print(data)
