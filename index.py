# Abdul-Basit-Ansari

# pip install gtts
from gtts import gTTS
# pip install playsound
from playsound import playsound

audio = 'speech.mp3'
lang = 'en'
# txt = input("Enter Your Text Here : ")
sp = gTTS(text="Enter Your Text Here : ",lang=lang, tld='com.in',slow=False)

sp.save(audio)
playsound(audio)