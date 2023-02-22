from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
lang = 'en'
sp = gTTS(text='''enter your text here
''',lang=lang, tld='com.in',slow=False)

sp.save(audio)
playsound(audio)