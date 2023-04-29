"""
Summarize a long text document
"""
import os

from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import TextLoader
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()


CHAIN_TYPE = os.getenv("CHAIN_TYPE", "map_reduce")
# Number of tokens per chunk to split the text into.  The larger the chunk size
# the more context the LLM has to work with.
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
# Number of tokens each chunk should overlap.  This helps the LLM
# understand the context of the text.
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "100"))
# Temperature: Value between 0 - 1.  The higher the temperature the more
# variability there will be in the output.
LLM_TEMPERATURE = int(os.getenv("LLM_TEMPERATURE", "1"))
# Your OpenAI API key - it needs a billing method or account credits
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Path to the text file to summarize
TEXT_TO_SUMMARIZE = os.getenv("TEXT_PATH")

# Load your text content
loader = TextLoader(TEXT_TO_SUMMARIZE)
documents = loader.load()

# Split the text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# Initialize the LLM with some randomness and then summarize the text chunks
# Each chunk is summarized and then a summary is made of all summaries
llm = OpenAI(temperature=LLM_TEMPERATURE, openai_api_key=OPENAI_API_KEY)
chain = load_summarize_chain(llm, chain_type=CHAIN_TYPE, verbose=True)
chain.run(texts)
