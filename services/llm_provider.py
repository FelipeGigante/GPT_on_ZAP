from openai import OpenAI
import os
from dotenv import load_dotenv

# constants
MODEL = "gpt-4.1"
load_dotenv()

class LLM_PROVIDER():
    
    def __init__(self):
        self.openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def send_message(self, message):
        
        responses = self.openai.responses.create(
            model=MODEL,
            input=message
        )

        return responses.output_text
        