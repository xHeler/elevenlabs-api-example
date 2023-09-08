import os
from elevenlabs import set_api_key, generate, save
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

set_api_key(api_key)

audio = generate(
  text="Witam, jestem modelem mówiącym po polsku.",
  voice="Bella",
  model="eleven_multilingual_v2"
)

save(audio, "voice.wav")