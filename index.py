# Abdul-Basit-Ansari

from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
lang = 'en'
txt = input("enter your text here")
sp = gTTS(text=txt,lang=lang, tld='com.in',slow=False)

sp.save(audio)
playsound(audio)