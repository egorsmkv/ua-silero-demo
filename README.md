# Speech-to-Text for the Ukrainian language based on Silero

This is a repository with demonstration code that uses [the Silero Model for Ukrainian](https://github.com/snakers4/silero-models) 
in the task of Speech-to-Text recognition.

### How to run

#### Linux

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

#### Windows

1. Install Anaconda (from: https://www.anaconda.com/products/individual#windows)

2. Run Anaconda Powershell Prompt

3. Install PyTorch and other libraries:

    ```
    conda install pytorch torchvision torchaudio cpuonly -c pytorch
    ```

4. Install other libraries:

    ```
    pip install SoundFile
    ```

Run the demos:

```
cd C:\path\to\project

python .\test_official_demo.py
python .\own_recodings_demo.py
```

It was tested on Windows x64 only.
