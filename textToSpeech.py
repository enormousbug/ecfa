import os
from elevenlabs.client import ElevenLabs

def textToSpeech(text):
  client = ElevenLabs(api_key=os.getenv('ELEVENLABS_API_KEY'))
  audio = client.generate(text=text, voice="", model="")
  return audio