#==============Start==============================#

import speech_recognition as sr
import time
from gtts import gTTS
from tempfile import TemporaryFile
from pygame import mixer

# The function
def function():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('====speak===((((0))))')
        audio=r.listen(source)
        return audio
    try:
        text=r.recognize_google(audio)
        print("you said : {}".format(text))
           
            
    except:
        print("sorry")
'''        
def reply():
    if (text=='help'):
         mixer.init()
         tts=gTTS('Hello')
         sf=TemporaryFile()
         tts.write_to_fp(sf)
         sf.seek(0)
         mixer.music.load(sf)
         mixer.music.play()
'''

        
        
#=================================================#


#Main loop
while True:
    function()
#    reply()


    
#==============End=================================#
