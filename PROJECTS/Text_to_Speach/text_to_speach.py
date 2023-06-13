#pip install elevenlabslib
from elevenlabslib import *
api = ElevenLabsUser("2a4e9c5178c68739db794e528c97cf0c")  # API key copied from Elevenlabs website

voice = api.get_voices_by_name("Sam")[0]
text = input("Enter text to speak:")
def gen_voice(text):
    voice.generate_and_play_audio(text,playInBackground=False)
gen_voice(text)
