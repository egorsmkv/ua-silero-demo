# Speech-to-Text for the Ukrainian language based on Silero

This is a repository with demonstration code that uses [the Silero Model for Ukrainian](https://github.com/snakers4/silero-models) 
in the task of Speech-to-Text recognition.

### How to run

Install dependencies and enter the python environment:

```
pipenv install
pipenv shell
```

Run the demos:

```
python test_official_demo.py
python own_recodings_demo.py
```

### Other

#### Convert a file to the PCM wav file 

```
ffmpeg -i input.mp3 -acodec pcm_s16le -ac 1 -ar 16000 output.wav
```
