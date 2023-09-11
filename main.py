import os
from elevenlabs import set_api_key, generate, save, Voice
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

set_api_key(api_key)
voice_id = "fK7vc9jYL8ZMq0lD4VfK"

story = """Once upon a time, in a lush meadow nestled between two towering oak trees, 
there lived an industrious ant named Andy. He was known throughout the meadow for his diligence and foresight. 
All day long, Andy would toil, gathering grains and seeds to store for the upcoming winter. 
He believed in the importance of hard work and planning for the future."""


audio = generate(
    text=story,
    voice=Voice(voice_id=voice_id),
    model="eleven_multilingual_v2"
)

save(audio, "voice.wav")
