# import os
# from dotenv import load_dotenv
# from deepgram import DeepgramClient, SpeakOptions
# from playsound import playsound

# load_dotenv()

# class TTS:
#     def __init__(self):
#         self.filename = "output.wav"
    
#     def speak(self, text):
#         try:
#             # STEP 1: Create a Deepgram client using the API key from environment variables
#             deepgram = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))

#             # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
#             options = SpeakOptions(
#                 model="aura-asteria-en",
#                 encoding="linear16",
#                 container="wav"
#             )

#             # STEP 3: Call the save method on the speak property
#             SPEAK_OPTIONS = {"text": text}
#             response = deepgram.speak.v("1").save(self.filename, SPEAK_OPTIONS, options)

#             # STEP 4: Play the audio file
#             playsound(self.filename)

#         except Exception as e:
#             print(f"Exception: {e}")

# if __name__ == "__main__":
#     tts = TTS()
#     tts.speak("Hello, how can I help you today?")
# from gtts import gTTS
# import os

# def speak(text, lang):

#     tts = gTTS(text=text, lang=lang)

#     tts.save("response.mp3")

#     os.system("start response.mp3")

from gtts import gTTS
from googletrans import Translator
import os

translator = Translator()

def speak(text, lang):

    # translate response if Telugu
    if lang == "te":

        text = translator.translate(text, dest="te").text

    # translate response if Hindi
    elif lang == "hi":

        text = translator.translate(text, dest="hi").text

    print("Assistant speaking:", text)

    tts = gTTS(text=text, lang=lang)

    tts.save("response.mp3")

    os.system("start response.mp3")
