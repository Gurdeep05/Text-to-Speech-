from gtts import gTTS
import os

f = open('text.txt')
a = f.read()

language = 'en'
audio = gTTS(text = x,lang = language , slow = False)

audio.save('speech.wav')
os.system('speech.wav')
