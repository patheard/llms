.PHONY: run install

run:
	whisper $(AUDIO) --language en --model $(MODEL)

install:
	sudo apt update &&\
	sudo apt install -y ffmpeg &&\
	pip install --user -r requirements.txt
