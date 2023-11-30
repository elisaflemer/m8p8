import os
import dotenv
from openai import OpenAI
from pathlib import Path
from playsound import playsound
import argparse
import wave
import sounddevice as sd
import numpy as np

dotenv.load_dotenv()
client = OpenAI()

def record_audio(file_path, duration=5, sample_rate=44100):
    print("Recording...")

    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.int16)
    sd.wait()

    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

    print(f"Audio recorded and saved to {file_path}")

def transcribe_and_translate_audio(file_path):
    with open(file_path, "rb") as file:
        translation = client.audio.translations.create(
            model="whisper-1", file=file
        )
    return translation.text

def speak(text):
    speech_file_path = Path(__file__).parent / "output.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    response.stream_to_file(speech_file_path)

parser = argparse.ArgumentParser(description='Transcribe and translate audio, then generate speech.')
parser.add_argument('--file_path', type=str, help='Path to the audio file for transcription and translation')

args = parser.parse_args()
file_path = args.file_path

if file_path:
    translation = transcribe_and_translate_audio(file_path)
else:
    record_audio('recording.mp3')
    translation = transcribe_and_translate_audio('recording.mp3')

print('TRANSLATION:', translation)
speak(translation)
playsound('output.mp3')
