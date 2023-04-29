# Ingest :llama:
Use LlamaIndex to augment an LLM with our own data.  This is the [LLamaIndex starter tutorial](https://gpt-index.readthedocs.io/en/latest/getting_started/starter_example.html) which adds an [essay by Paul Graham](http://paulgraham.com/worked.html) to ChatGPT's context so we can ask questions about it.

1. Loads the essay content and creates a vector index.
1. Queries the index. 

## Setup
- `cp .env.example .env`
- Add your OpenAI API key.
- `make install && make run`

# Cost
~$0.01 to create the index and query it.

# Docs
- [LLamaIndex starter tutorial](https://gpt-index.readthedocs.io/en/latest/getting_started/starter_example.html)