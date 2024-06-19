from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access and store environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")