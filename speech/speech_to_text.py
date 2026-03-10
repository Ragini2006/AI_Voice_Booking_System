'''
This module captures audio from the user's microphone and converts it into text using Google's Speech recognition API. It also detects the language of the transcribed text to help the assistant respond in the appropriate language. The function `transcribe()` listens for audio input, processes it, and returns both the transcribed text and the detected language code.
'''
import speech_recognition as sr
from langdetect import detect

def transcribe():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)

        lang = detect(text)

        return text, lang

    except Exception as e:
        print("Speech recognition failed:", e)
        return "", "en"
