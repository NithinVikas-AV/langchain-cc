from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
import os

"""
Setup Instructions (same as original):
1. Create Firebase project
2. Enable Firestore
3. Install & authenticate Google Cloud CLI
4. Enable Firestore API
5. Install required packages:
   pip install langchain-google-genai langchain-google-firestore google-cloud-firestore python-dotenv
"""

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Firebase Firestore setup
PROJECT_ID = "<project_id>"  # Replace with your actual project ID
SESSION_ID = "<session_id>"
COLLECTION_NAME = "<collection_name>"

# Initialize Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# Initialize Gemini Chat Model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key,)
  # Ensures compatibility with SystemMessage

# Start Chat Loop
print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    # Add user message to Firestore
    chat_history.add_user_message(human_input)

    # Generate response from Gemini
    ai_response = model.invoke(chat_history.messages)

    # Save AI response to Firestore
    chat_history.add_ai_message(str(ai_response.content))

    print(f"AI: {ai_response.content}")
