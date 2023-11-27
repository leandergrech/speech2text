import os
from recorder import record_audio
from transcriber import get_deepspeech_model, transcribe_audio


def main():
    model = get_deepspeech_model()

    temp_wav_file = 'temp.wav'

    record_audio(record_seconds=5, wav_output_fn=temp_wav_file)
    text = transcribe_audio(temp_wav_file, model=model)

    os.remove(temp_wav_file)

    print("Transcribed text:", text)


if __name__ == "__main__":
    main()
