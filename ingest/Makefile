.PHONY: run fmt install

run:
	python ingest.py

fmt:
	black . --target-version py39

install:
	pip install --user -r requirements.txt
