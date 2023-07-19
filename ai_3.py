from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
text=input('Enter a text : ')
tts=gTTS(text)
mixer.init()
sf=TemporaryFile()
tts.write_to_fp(sf)
sf.seek(0)
mixer.music.load(sf)
mixer.music.play()
