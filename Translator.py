from googletrans import Translator
from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
translator=Translator()
word=input("Enter word in En : ")
tts=gTTS(text=translator.translate(word, dest="ar").text,lang="ar")
mixer.init()
sf=TemporaryFile()
tts.write_to_fp(sf)
sf.seek(0)
mixer.music.load(sf)
mixer.music.play()
