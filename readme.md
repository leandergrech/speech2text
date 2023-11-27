# Installation
The speech2text models need to be downloaded before running any script. The `pbmm` file is ~189MB and the `scorer` file is ~953MB.
```
conda create -n myenv python=3.9
sudo apt-get install portaudio19-dev -y
pip install -r requirements.txt
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```

# Usage
 - `example.py` will listen to `turnoffthelightsinthebedroom.wav` and produces a transcription.
 - `record_transcribe.py` will record audio for 5 seconds and converts to text using the `deepspeech` package.