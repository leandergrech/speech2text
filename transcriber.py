import numpy as np
import wave
import deepspeech
from params import MODEL_FILE_PATH, SCORER_FILE_PATH


def get_deepspeech_model():
    model = deepspeech.Model(MODEL_FILE_PATH)
    model.enableExternalScorer(SCORER_FILE_PATH)

    return model


def transcribe_audio(wave_input_fn, model=None):
    if model is None:
        model = get_deepspeech_model()

    with wave.open(wave_input_fn, 'rb') as wf:
        frames = wf.getnframes()
        buffer = wf.readframes(frames)
        data16 = np.frombuffer(buffer, dtype=np.int16)

    return model.stt(data16)
