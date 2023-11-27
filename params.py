from pyaudio import paInt16

# Recording parameters
FORMAT = paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024

# Model files
MODEL_FILE_PATH = 'deepspeech-0.9.3-models.pbmm'
SCORER_FILE_PATH = 'deepspeech-0.9.3-models.scorer'
