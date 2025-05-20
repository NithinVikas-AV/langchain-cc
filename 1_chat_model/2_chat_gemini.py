from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Create a Gemini chat model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key,)

# First interaction
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from Gemini: {result.content}")

# Second interaction with message history
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]

# Invoke the model again with updated context
result = model.invoke(messages)
print(f"Answer from Gemini: {result.content}")
