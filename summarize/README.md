# Summarize :open_book:
Takes a long text and summarizes it.  Does this by:
1. Splitting the text into fixed sized token chunks with some overlap.
1. Summarizes each chunk.
1. Summarizes the summaries.

## Setup
- `cp .env.example .env`
- Add your OpenAI API key and path to the text file you want to summarize.
- `make install && make run`

# Cost
~$1 for a 100,000 character text doc.

# Docs
- [Summarize chain example](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)