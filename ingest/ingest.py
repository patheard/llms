"""
Creates a vector index and queries it.
"""
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from dotenv import load_dotenv

load_dotenv()

documents = SimpleDirectoryReader("data").load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

response = index.query("What did the author do growing up?")
print(response)
