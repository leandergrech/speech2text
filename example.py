import os
from recorder import record_audio
from transcriber import get_deepspeech_model, transcribe_audio


def main():
    model = get_deepspeech_model()

    wav_file = 'turnoffthelightsinthebedroom.wav'

    print(f'Listening to: {wav_file}')

    text = transcribe_audio(wav_file, model=model)

    print("Transcribed text:", text)


if __name__ == "__main__":
    main()
