import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load your API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Correct way to initialize with API key
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,  # THIS is critical
)

# Test it
response = model.invoke("what is 900 divided by 9")
print("Full Chat:")
print(response)
print("Content:")
print(response.content)