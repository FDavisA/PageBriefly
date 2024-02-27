import os

# Configuration and constants
URLS = ["https://www.storylane.io/"]
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4"
# MODEL_NAME = "gpt-3.5-turbo-instruct"
TEMPERATURE = 1
CHUNK_SIZE = 3000
CHUNK_OVERLAP = 200