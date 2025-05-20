from google.cloud import firestore

client = firestore.Client(project="langchain-cc")
docs = list(client.collections())
print(f"Available collections: {[c.id for c in docs]}")
