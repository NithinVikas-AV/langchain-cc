from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Create a Gemini model (with system message support workaround)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key,)

chat_history = []  # Store messages

# Set an initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query))  # Add user input

    # Invoke model with full history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  # Add model response

    print(f"AI: {response}")

# Print message history after exiting
print("---- Message History ----")
print(chat_history)
