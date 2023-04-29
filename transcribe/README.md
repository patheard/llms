# Transcribe :memo:
Uses OpenAI Whisper to transcribe audio files.  This is useful when you want to provide more context to an LLM.

## Setup
```sh
make install
make run AUDIO=path/to/audio/file MODEL=<tiny|base|small|medium|large>
```
:warning: The larger the model, the [better and slower](https://github.com/openai/whisper#available-models-and-languages) the transcription.

## Cost
Free, apart from time.

## Docs
- [OpenAI Whisper](https://github.com/openai/whisper)